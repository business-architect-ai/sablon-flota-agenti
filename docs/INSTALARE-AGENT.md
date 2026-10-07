# Instalarea unui agent în flotă

Procedura de adăugare a unui agent nou, fie construit de la zero cu `onboarding-agent`, fie
luat din biblioteca de agenți.

**Se face în mod atelier, cu flota oprită.** Vezi `METODOLOGIE.md`. Dacă instalezi în timp ce
flota rulează, orchestratorul nu va ști de agentul nou până la repornire, iar tu vei crede că
instalarea a eșuat.

## Decizia de versiune: rămânem pe v2.0

**Decis 2026-10-05.** Linia de orchestrare rămâne pe `onboarding-agent` v2.0, cel cu `FLUX.md`
și fără lacăt. Nu aducem v3.1 aici și nu migrăm agenții existenți.

Motivul: subiectul e orchestrarea, cine vorbește cu cine și unde ajunge munca. Lacătul din
v3.1 aduce trei piese care pot pica pe o mașină străină (Python, hook-uri, subagent), niciuna
nu e necesară pentru orchestrare, iar procedura lui de migrare e netestată, inclusiv pe
Windows.

Un agent v2 e corect așa cum e: `FLUX.md` ține și pașii, și criteriile („Verific înainte să
livrez"), o singură meserie, fără skill-uri, deci o singură sursă pentru fiecare întrebare.

**Nevoile de evaluare se acoperă cu un evaluator**, nu cu lacătul. Fără lacăt, chemarea
evaluatorului rămâne voluntară, iar singura verificare impusă e cea a orchestratorului:
fișierul există și nu e gol. E un compromis asumat, nu o omisiune.

## Prefixele ocupate

Prefixul unui agent e numele folderului lui și, în același timp, numele rolului în flotă.
Ocupate acum:

```
copywriter  creator-carusele  director-marketing  orchestrator
publisher  research-strategie  web-designer
```

Verifică lista pe disc înainte, nu din memorie:

```
for d in */; do [ -f "$d/CLAUDE.md" ] && echo "$d"; done
```

Atenție dacă pe aceeași mașină rulează o a doua flotă cu aceleași prefixe de rol. De-aia orchestratorul nu trimite niciodată pe nume, ci pe adresa de
socket dată de `orchestrator/scripts/flota.sh`.

## Cei șapte pași

**1. Verifici prefixul.** Dacă agentul nou are un nume deja ocupat, îl redenumești acum, nu
după ce l-ai conectat. O coliziune de rol se vede târziu și se manifestă ca mesaje care ajung
la agentul greșit.

**2. Copiezi folderul** în rădăcina flotei, cu numele prefixului alese la pasul 1.

**3. Te uiți ce formă are, nu îl converti.** `SABLON-AGENT.md` descrie convenția flotei:
șase fișiere plus folderele de lucru. Agenții construiți cu `onboarding-agent` în versiunea
curentă vin cu mai mult: opt fișiere (`FLUX.md` pentru cum lucrează, `VERIFICARE.md` pentru
când a terminat bine) plus trei piese de mașinărie, un subagent evaluator în `.claude/agents/`,
un script de verificare în `unelte/` și lacătul `unelte/lacat.py`, pornit de hook-urile din
`.claude/settings.json`. Are nevoie de Python 3.8 sau mai nou.

**Nu scoți nimic din ele.** Verifici un singur lucru, după regula „fluxul stă într-un singur
loc" din `METODOLOGIE.md`:

| Ce are agentul | Ce faci |
|---|---|
| `FLUX.md` și `VERIFICARE.md`, fără skill-uri | îl lași exact așa, e corect |
| skill-uri, fără `FLUX.md` | îl lași exact așa, e corect |
| **`FLUX.md` și skill-uri care descriu aceiași pași** | repari **înainte** de instalare, vezi mai jos |

Reparația: skill-ul câștigă pentru tot ce acoperă. Pașii din `FLUX.md` se mută în skill și
fișierul se retrage, iar criteriile din `VERIFICARE.md` se mută la pasul de verificare al
skill-ului. Scoți din lista de lectură din `CLAUDE.md` ce ai retras.

Despre lacăt, dacă agentul îl are: **nu încerci să-i editezi scripturile.** Regulile `deny` din
`.claude/settings.json` refuză scrierea în ele, și e corect să fie așa, altfel lacătul nu mai
e lacăt. Aducerea lor la zi se face rulând din nou `onboarding-agent` pe folderul agentului,
care are procedură scrisă pentru asta.

**4. Îi scrii contractul cu folderul comun.** În `TOOLS.md`, explicit: ce citește din
`campanie/`, ce fișiere scrie, și regula că nu scrie niciodată în folderul altui agent. Un
agent fără contract scrie unde nimerește, iar asta se descoperă după ce a suprascris ceva.

**5. ÎL ÎNSCRII ÎN TABELUL DE PREZENȚĂ AL ORCHESTRATORULUI.** În `orchestrator/CLAUDE.md`,
la „Apelul de prezență", rol și prefix. Dacă pasul are vreun loc în lanțul unei campanii, îl
adaugi și în tabelul „Lanțul unei campanii", cu ce așteaptă înainte și ce produce.

**6. REPORNEȘTI ORCHESTRATORUL.** Altfel rulează cu tabelul vechi și agentul nou nu există
pentru el.

**7. Îl testezi singur, înainte de lanț.** O sarcină de un pas, dată de mână, în fereastra
lui. Verifici că citește ce trebuie, scrie unde trebuie și raportează. Dacă nu trece testul
singur, nu intră în lanț.

## Pașii 5 și 6 sunt cei care se sar

Un agent instalat fără pașii 5 și 6 **există și e invizibil.** Pornește, răspunde dacă îi
scrii tu direct, și orchestratorul nu îl cheamă niciodată, pentru că nu știe de el. Pare o
problemă de agent, e o problemă de registru.

Aceeași greșeală a apărut la distribuția de skilluri în CortexTOS: instalate corect, dar
acolo unde nimeni nu citește. Instalarea nu e copierea fișierelor, e copierea **plus
înscrierea în registru plus repornirea cititorului de registru.**

## După instalare

Treci în mod flotă după procedura din `METODOLOGIE.md`: închizi tot, deschizi fiecare agent,
apel de prezență, și abia apoi prima sarcină. La apel trebuie să apară și agentul nou. Dacă nu
apare, te-ai oprit la pasul 5 sau 6.

Dacă agentul a fost repornit după ce flota era deja pornită, adresa lui s-a schimbat: rulează
din nou `orchestrator/scripts/flota.sh`.

## Livrabilele care se adună în mai multe ture

Dacă agentul își construiește livrabilul pe bucăți, în mai multe ture (culege de pe web, se
oprește să întrebe, primește completări), scrie în `CLAUDE.md`-ul lui regula ciornelor: lucrează
în `ciorne/<nume>.md` și scrie fișierul declarat din `../campanie/livrabile/` abia când e gata.

Motivul se vede numai la agenții cu lacăt, dar regula e bună la toți. La un agent cu lacăt, o tură
care se termină cu o jumătate de livrabil în fișierul declarat îi cere verificarea unui text
neterminat: textul pică și consumă o rundă de reparare pe ceva ce nu era gata. La un agent fără
lacăt, un livrabil pe jumătate în fișierul declarat îl face pe orchestrator să treacă la pasul
următor, fiindcă el verifică doar că fișierul există și nu e gol.

## Dacă construiești un agent pe v3.1: ce urmărești la întrebări

Skill-ul pune întrebările, dar două răspunsuri pot strica evaluatorul fără să se vadă până la
prima rulare. Le refuzi pe loc, nu le repari după.

**Întrebările de judecată trebuie să stea singure.** O întrebare formulată relativ la mostră („e
la fel de aprofundat ca exemplul", „are aceeași structură") nu se poate răspunde, fiindcă
evaluatorul vede livrabilul și criteriile, nu un etalon de comparat. Rezultatul e NESIGUR la
fiecare rulare, adică un evaluator care nu spune nimic și pe care înveți să-l ignori. Formulezi
criteriul în sine: nu „la fel de aprofundat ca exemplul", ci ce anume face un livrabil aprofundat.

Testul pe care îl aplici fiecărei întrebări: se poate răspunde la ea **numai din livrabil și din
sursă**? Dacă răspunsul cere să te uiți la mostră, întrebarea e prost formulată. Verificarea
skill-ului pe mostra bună nu prinde cazul ăsta, fiindcă mostra seamănă cu ea însăși și o întrebare
relativă la ea iese mereu TRECE. Deci refuzul tău pe loc e plasa, nu un pas automat.

Mostrele arată ce înseamnă întrebările, nu sunt un tipar de copiat. Evaluatorul nu compară
livrabilul cu ele la lungime, structură sau subiect, iar lungimea o verifică scriptul. Din
2026-10-06 asta e scris explicit în șablonul skill-ului, deci agenții construiți de acum încolo o
au în prompt.

**Regulile numărabile trebuie să se potrivească cu de unde vin datele.** Exemplul concret: o regulă
de tip „fiecare cifră apare în sursă" nu merge la un agent care culege de pe web, fiindcă nu există
un fișier sursă, și ar pica pe orice cifră reală. Skill-ul avertizează și n-o propune când
livrabilul are în mod firesc numere din afară, dar dacă apare, o refuzi. Pentru research, regula
corectă e că fiecare afirmație are o sursă și fiecare sursă se deschide, nu că cifrele se regăsesc
într-un fișier.
