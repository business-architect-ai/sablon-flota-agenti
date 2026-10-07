# Scriptul de resetare a campaniei, specificație

## Ce construiești

Un script, `campanie/reseteaza.sh`, care pregătește folderul comun pentru o lucrare nouă,
fără să piardă nimic. Îl rulează omul sau o sesiune la cererea lui. Agenții din flotă nu îl
rulează niciodată.

> **Nescris.** Documentul ăsta e specificația, nu scriptul. În flota din care vine șablonul,
> resetarea s-a făcut de mână. Dacă îl implementezi, citește întâi secțiunea despre ce rămâne
> neatins: `brand/` și `brief/` sunt intrări și nu se șterg.

Problema: după o rulare, în `campanie/` rămân livrabilele vechi. Poarta Orchestratorului
verifică doar că un fișier există și nu e gol, deci un `copy.md` de ieri trece drept nou, iar
un agent poate porni pe el. Resetarea de mână e ușor de făcut pe jumătate.

## Structura de acum a `campanie/`

```
brand/        CITESTE.md, voce.md, vizual.md          intrare, rămâne
brief/        brieful omului                          intrare, rămâne
strategie/    avatare, nivel-constientizare, metoda, plan-campanie, brief-uri
livrabile/    research.md, copy.md, carusel.md, carusel/, landing.md,
              directie-vizuala.md, landing/, postari.md, postari/
dashboard/    pagina de proiector                     unealtă, rămâne
stare.md      tabla                                   se resetează
stare.json    tabla, pentru dashboard                 se resetează
```

## Ce face

1. **Arhivează** tot ce e rezultat al rulării în `campanie/_rulari/AAAA-LL-ZZ-HHMM-<eticheta>/`,
   păstrând structura (`strategie/`, `livrabile/`, `stare.md`, `stare.json`). Eticheta vine ca
   argument (`./reseteaza.sh repetitie`). Fără argument, eticheta e `rulare`.
2. **Păstrează ca intrare** pentru rularea următoare:
   - `brand/` și `brief/`, întotdeauna, neatinse;
   - `livrabile/research.md`, dacă se dă `--pastreaza-research` (research-ul e de obicei pregătit
     dinainte);
   - din `strategie/`, **doar fișierele care au pe primul rând `<!-- APROBAT`**. Celelalte se
     arhivează și se scot.
   Ce se păstrează se copiază și în arhivă, ca arhiva să fie completă.
3. **Golește** restul din `strategie/` și `livrabile/`. Folderele rămân, goale.
4. **Resetează tabla:** rescrie `stare.md` și `stare.json` din două șabloane,
   `campanie/_sabloane/stare.md` și `campanie/_sabloane/stare.json`, pe care le creezi tu. Pornește
   de la structura actuală a `stare.md` (secțiunile „Acum”, tabelul pașilor, „Cum a decis
   echipa”, „Ce s-a întâmplat”, „Caruselul”, „Pagina”) și de la formatul din
   `dashboard/SPEC.md`. Starea inițială: toți pașii pe `asteapta`, „Acum: echipa așteaptă prima
   sarcină”, fără decizii și fără evenimente. Pașii păstrați ca aprobați apar cu starea
   `aprobat-dinainte`.
5. **Raportează** la final, în română: ce s-a arhivat și unde, ce s-a păstrat ca intrare, ce s-a
   golit.

## Siguranță

- **Implicit rulează pe uscat** (`--simulare` e comportamentul standard): afișează ce ar face,
  fără să mute nimic. Mută efectiv doar cu `--executa`.
- **Nu șterge nimic definitiv.** Doar mută în arhivă. Dacă arhiva nu s-a scris complet (verifici
  numărul de fișiere), nu golește nimic și se oprește cu mesaj clar.
- Nu atinge `brand/`, `brief/`, `dashboard/`, `_rulari/`, `_sabloane/` și nimic din afara `campanie/`.
- Ignoră `.DS_Store`.
- Se poate rula din orice folder: calculează calea `campanie/` din locul scriptului.

## Constrângeri

- `bash` compatibil cu macOS (fără opțiuni GNU la `sed`, `cp`, `date`) sau `python3` din sistem,
  fără pachete instalate.
- Mesajele în română, cu diacritice. Fără emoji. Fără liniuță lungă.

## Cum verifici

1. Fă o copie a `campanie/` în `/tmp/campanie-test/` și testează doar acolo, cu scriptul copiat
   lângă ea.
2. Cazuri: rulare pe uscat (nu se mișcă nimic); execuție cu și fără `--pastreaza-research`; o
   strategie cu doi pași `APROBAT` și trei neaprobați; o a doua execuție imediat după prima
   (nu strică nimic, arhivează o rulare goală sau spune că nu are ce arhiva); `stare.json`
   rezultat e JSON valid și dashboard-ul îl afișează (`?sursa=` din `dashboard/SPEC.md`).
3. Nu rulezi scriptul pe `campanie/` reală. Asta o face Dănuț.

## Ce nu faci

- Nu modifici fișierele agenților, `CLAUDE.md`-urile sau dashboard-ul.
- Nu pornești și nu oprești agenți.
