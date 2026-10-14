# Șablon de flotă de agenți în Claude Code

O flotă e un grup de sesiuni Claude Code obișnuite, fiecare pornită în folderul ei, care își
trimit sarcini între ele prin `ListAgents` și `SendMessage`. Nu e nevoie de runtime, de
server sau de orchestrator extern. Șablonul ăsta conține partea care nu se construiește
singură: **orchestratorul**, **contractul folderului comun** și **documentația de lucru**.

## Ce e aici și ce nu

| Ai | Nu ai |
|---|---|
| orchestratorul, cu regulile lui | roluri gata făcute |
| scheletul unui rol, de completat | conținut de lucrare (texte, imagini, research) |
| folderul comun și contractul lui | fișele de brand ale cuiva |
| scriptul de adrese și cel de contract | memoria vreunei flote care a rulat deja |
| metodologia și ghidul de instalare | dependențe: fără Python, fără hook-uri |

Rolurile **nu** vin gata făcute, fiindcă un rol copiat de la altcineva are fișa altcuiva, și
se vede imediat în livrabile. Ce primești e `agent-sablon/`, cele șase fișiere ale unui rol cu
locurile de completat, plus folderele de lucru. Îl copiezi o dată pentru fiecare rol și îl
completezi.

Partea care nu se copiază, meseria rolului, o scrii tu. Dacă vrei, o scrii **conversațional**:
deschizi o sesiune în folderul rolului și ceri să fii întrebat, fișier cu fișier, despre ce
face rolul. Întrebările sunt în `docs/SABLON-AGENT.md`, la fiecare fișier.

Orchestratorul vine completat, cu mecanismul lui întreg, fiindcă el e la fel în orice flotă.
Ce diferă la el sunt numele rolurilor și ale livrabilelor, iar alea sunt locurile `<...>`.

## Cum pornești

1. Clonează repo-ul și dă-i numele flotei tale. Folderul în care îl pui devine rădăcina
   flotei: orchestratorul și fiecare rol stau ca subfoldere ale lui, lângă `campanie/`.
2. Scrie în `orchestrator/roluri.txt` prefixele rolurilor tale, câte unul pe linie. Vin
   completate cu exemplul de marketing, le înlocuiești.
3. Completează locurile marcate cu `<...>` din `orchestrator/CLAUDE.md`, `USER.md`,
   `MEMORY.md` și `TOOLS.md`. Restul textului e mecanismul și merge așa cum e.
4. Pentru fiecare rol, copiază `agent-sablon/` în folderul rolului și completează cele șase
   fișiere. Citește înainte `docs/SABLON-AGENT.md`, care spune la ce e fiecare fișier și ce
   greșeală face dacă e scris prost, și `docs/INSTALARE-AGENT.md` pentru procedură.
   Exemplu, pentru un rol numit `documentare`:

       cp -R agent-sablon documentare

5. Adaptează numele de fișiere din `orchestrator/scripts/verifica_livrabil.py` la livrabilele
   flotei tale. Logica rămâne, numele se schimbă.
6. Deschide o sesiune în `orchestrator/` și cere-i apelul de prezență.

## Documentația

`docs/METODOLOGIE.md`, **citește-o prima.** Explică de ce modul atelier și modul flotă se
exclud, și de ce o sesiune pornită nu recitește fișierele pe care i le editezi sub ea.

`docs/INSTALARE-AGENT.md`, cum construiești un rol și la ce te uiți în întrebările pe care
ți le pune skill-ul.

`docs/SABLON-AGENT.md`, la ce e fiecare dintre cele șase fișiere ale unui rol și ce greșeală
face dacă e scris prost. Îl citești în timp ce completezi `agent-sablon/`.

`docs/spec-reset-campanie.md`, specificația unui script de golire a folderului comun între
două lucrări. **Scriptul nu e scris**, documentul explică doar problema și ce nu se atinge.

`docs/exemplu-flota-marketing.md`, o flotă completată, cu cinci roluri și lanțul ei.

## Două lucruri care se învață greu

**Verificarea se împarte după ce poate vedea cine.** Un agent își verifică meseria, pentru
că doar el știe ce a vrut să scrie. Orchestratorul verifică ce trebuie să se potrivească
între fișiere scrise de agenți diferiți, pentru că doar el le vede pe amândouă. Nu e o
preferință, e o imposibilitate: un agent nu poate verifica un fișier pe care nu îl deschide.

**Raportul unui agent nu e un fapt.** E scris de cel care a produs livrabilul, deci poate fi
înmuiat sau greșit fără rea intenție. Faptul e chitanța scrisă de cod, pe care agentul nu are
voie să o scrie. Regulile din `orchestrator/CLAUDE.md` citesc chitanța, nu raportul.
