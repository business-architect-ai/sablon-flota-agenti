#!/usr/bin/env python3
"""Verifica CONTRACTUL unei campanii, nu meseria agentilor.

Il ruleaza Orchestratorul pe folderul de livrabile, inainte sa porneasca pasul
urmator. Ce verifica aici nu poate fi verificat de niciun agent: fiecare agent
vede doar fisierul lui, iar consistenta dintre livrabile se vede doar de aici.

Nu verifica stilul, nu da note si nu judeca calitatea. Toate rezultatele sunt
fapte: un text declarat apare sau nu apare.

    python3 orchestrator/scripts/verifica_livrabil.py campanie/livrabile
    python3 orchestrator/scripts/verifica_livrabil.py campanie/livrabile --strict

Cod de ieșire: 0 curat, 1 abatere de contract, 2 eroare de chemare.
--strict face din avertismente abateri.

ȘABLON. Numele de fișiere din constantele de mai jos (FOI, INDEXURI și restul)
sunt cele ale flotei de marketing dată ca exemplu. Pentru flota ta le schimbi pe
ele, nu logica. Ce rămâne valabil e ideea: scriptul compară ce a declarat un
agent cu ce apare la alt agent, adică exact ce niciunul din ei nu poate vedea.
"""
import re
import sys
import unicodedata
from pathlib import Path

VERSIUNE = "1.0"

# `carusel.md` si `postari.md` sunt INDEXURI, nu livrabile de text. Textul care
# ajunge la public sta in fisiere-foaie. Un checker care caută in indexuri
# raporteaza abateri false.
FOI = ["postari/*/text.md", "landing/index.html"]
INDEXURI = {"carusel.md", "postari.md", "copy.md", "landing.md",
            "research.md", "directie-vizuala.md"}

# Declaratiile de indemn apar in doua formate in livrabilele reale, si amandoua
# sunt legitime. Fii permisiv la EXTRAGERE si strict la VERIFICARE: un parser
# blocat pe un layout raporteaza abateri false si se opreste dupa o zi.
#   (a) antet urmat de lista:  **Îndemnurile, ... :**  apoi  - piesa: text
#   (b) cate o linie per piesa: **Îndemnul paginii, ... :** text
TIPAR_ETICHETA = re.compile(r"^\*\*(Îndemn\w*[^*]*?):?\*\*[ \t]*(.*)$", re.M)
TIPAR_PIESA = re.compile(r"^[ \t]*-[ \t]*([^:]+):[ \t]*(.*)$")
FARA_INDEMN = re.compile(r"fără[ \t]+îndemn", re.I)

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⬀-⯿️]")
# s si t cu SEDILA (greșit) in loc de virgula dedesubt (corect)
SEDILA = re.compile("[şţŞŢ]")
UMPLUTURA = re.compile(r"\b(lorem ipsum|TODO|TBD|XXX|placeholder|de completat)\b", re.I)


# Fisierele reale amesteca ghilimele: „ (U+201E) la deschidere cu " (U+0022) la
# inchidere. Dezbracam pe caractere, nu pe perechi fixe, si normalizam si la
# comparare, ca o foaie care foloseste alt fel de ghilimele sa nu dea abatere falsa.
GHILIMELE = "\u201e\u201c\u201d\u2018\u2019\u00ab\u00bb\"'"


def ghilimele(t):
    """Scoate orice fel de ghilimele din jurul unui text declarat."""
    return t.strip().strip(GHILIMELE).strip()


def citeste_declaratia(copy_md):
    """Intoarce [(piesa, text_indemn sau None)], din oricare din cele doua formate."""
    text = copy_md.read_text(encoding="utf-8")
    linii = text.splitlines()
    piese = []
    for m in TIPAR_ETICHETA.finditer(text):
        eticheta, rest = m.group(1).strip(), m.group(2).strip()
        if rest:
            # formatul (b): declaratia e pe aceeasi linie
            piese.append((eticheta, None if FARA_INDEMN.search(rest) else ghilimele(rest)))
            continue
        # formatul (a): eticheta e antet, piesele vin ca lista imediat dupa
        i = text[:m.start()].count("\n") + 1
        while i < len(linii) and not linii[i].strip():
            i += 1
        while i < len(linii):
            p = TIPAR_PIESA.match(linii[i])
            if not p:
                break
            piesa, r = p.group(1).strip(), p.group(2).strip()
            piese.append((piesa, None if FARA_INDEMN.search(r) else ghilimele(r)))
            i += 1
    return piese or None


def foi_de_text(rad):
    gasite = []
    for tipar in FOI:
        gasite.extend(sorted(rad.glob(tipar)))
    return [f for f in gasite if f.is_file()]


def normalizeaza(t):
    """Compara textul fara sa cada pe forme Unicode diferite sau spatii multiple."""
    t = unicodedata.normalize("NFC", t)
    for g in "\u201e\u201c\u201d\u00ab\u00bb":
        t = t.replace(g, '"')
    for g in "\u2018\u2019":
        t = t.replace(g, "'")
    return re.sub(r"\s+", " ", t).strip()


class Neconfigurat(Exception):
    """Scriptul nu a fost adaptat la flota asta, sau flota n-a produs nimic.

    Nu e abatere de contract: nu spune nimic despre livrabile. De-aia iese cu 2,
    nu cu 1. Un `Nu porni pasul următor` pe un folder gol ar fi o oprire falsă.
    """


def verifica(rad, strict=False):
    abateri, avertismente = [], []
    copy_md = rad / "copy.md"

    if not copy_md.is_file():
        # Folder fără niciun livrabil: ori flota n-a produs încă nimic, ori
        # numele din constantele de sus sunt încă cele ale flotei-exemplu.
        if not [p for p in rad.iterdir() if p.is_file() and p.name != "CITESTE.md"]:
            raise Neconfigurat(
                "nu există niciun livrabil în {}.\n"
                "Dacă flota n-a produs încă nimic, e normal: nu ai ce verifica.\n"
                "Dacă a produs, atunci numele de fișiere din script sunt încă cele ale "
                "flotei-exemplu. Adaptează-le la livrabilele flotei tale (vezi comentariul "
                "din capul fișierului).".format(rad))
        return ["lipsește `copy.md`, nu există contract de verificat"], []

    foi = foi_de_text(rad)
    if not foi:
        avertismente.append(
            "niciun fișier-foaie găsit ({}), deci nu am ce compara. "
            "Pasul 4 încă n-a rulat?".format(", ".join(FOI)))

    # 1. CONTRACTUL: fiecare indemn declarat apare, cuvant cu cuvant, in cel
    #    putin o foaie. Asta e verificarea pe care doar Orchestratorul o poate face.
    piese = citeste_declaratia(copy_md)
    if piese is None:
        abateri.append(
            "`copy.md` nu are blocul „**Îndemnurile, textul exact, câte unul pe piesă:**”, "
            "deci îndemnurile nu se pot verifica în aval")
    else:
        texte_foi = {f: normalizeaza(f.read_text(encoding="utf-8", errors="replace"))
                     for f in foi}
        for piesa, indemn in piese:
            if indemn is None:
                continue
            cerut = normalizeaza(indemn)
            unde = [f for f, t in texte_foi.items() if cerut in t]
            if not unde and foi:
                abateri.append(
                    "îndemnul declarat pentru „{}” nu apare în nicio foaie: „{}”"
                    .format(piesa, indemn))
            elif unde:
                print("  îndemn „{}” găsit în: {}".format(
                    piesa, ", ".join(f.relative_to(rad).as_posix() for f in unde)))

    # 2. IGIENA, doar pe foi. Agentii din flota sunt pe v2 si n-au scripturi
    #    proprii, deci nimeni altcineva nu verifica lucrurile astea.
    for f in foi:
        t = f.read_text(encoding="utf-8", errors="replace")
        nume = f.relative_to(rad).as_posix()
        if "—" in t:
            abateri.append("{}: em dash, de înlocuit cu virgulă sau paranteze".format(nume))
        if SEDILA.search(t):
            abateri.append("{}: ș sau ț cu sedilă în loc de virgulă dedesubt".format(nume))
        for g in sorted(set(EMOJI.findall(t))):
            abateri.append("{}: emoji {!r}".format(nume, g))
        for g in sorted(set(m.group(0) for m in UMPLUTURA.finditer(t))):
            abateri.append("{}: umplutură rămasă, „{}”".format(nume, g))
        if "**" in t:
            avertismente.append(
                "{}: asteriscuri de bold, care nu au ce căuta în text publicat".format(nume))

    if strict:
        abateri.extend(avertismente)
        avertismente = []
    return abateri, avertismente


def main():
    arg = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--versiune" in sys.argv:
        print("verifica_livrabil.py {}".format(VERSIUNE))
        return 0
    if len(arg) != 1:
        print("Folosire: verifica_livrabil.py <folderul de livrabile> [--strict]")
        return 2
    rad = Path(arg[0]).expanduser()
    if not rad.is_dir():
        print("Nu e un folder: {}".format(rad))
        return 2

    print("Contract, în {}".format(rad))
    try:
        abateri, avertismente = verifica(rad, "--strict" in sys.argv)
    except Neconfigurat as e:
        print("  NECONFIGURAT: {}".format(e))
        return 2

    for a in avertismente:
        print("  DE PRIVIT: {}".format(a))
    for a in abateri:
        print("  ABATERE: {}".format(a))

    if abateri:
        print("\n{} abateri de contract. Nu porni pasul următor.".format(len(abateri)))
        return 1
    print("\nContractul e respectat{}.".format(
        ", {} de privit".format(len(avertismente)) if avertismente else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
