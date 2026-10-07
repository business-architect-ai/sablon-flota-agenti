# Șablon de flotă de agenți în Claude Code

O flotă e un grup de sesiuni Claude Code obișnuite, fiecare pornită în folderul ei, care își
trimit sarcini între ele prin `ListAgents` și `SendMessage`. Nu e nevoie de runtime, de
server sau de orchestrator extern. Șablonul ăsta conține partea care nu se construiește
singură: **orchestratorul**, **contractul folderului comun** și **documentația de lucru**.

## Ce e aici și ce nu

| Ai | Nu ai |
|---|---|
| orchestratorul, cu regulile lui | agenții specialiști |
| folderul comun și contractul lui | conținut de lucrare (texte, imagini, research) |
| scriptul de adrese și cel de contract | fișele de brand ale cuiva |
| metodologia și ghidul de instalare | memoria vreunei flote care a rulat deja |

Specialiștii **nu** sunt în șablon fiindcă nu se copiază, se construiesc. Pentru fiecare rol
rulezi skill-ul `onboarding-agent`, care îți pune întrebări despre meseria rolului și scrie
el `CLAUDE.md`, `IDENTITY.md`, `VERIFICARE.md`, `SOUL.md`, `USER.md`, `TOOLS.md`,
`MEMORY.md`, subagentul evaluator, scriptul de verificare și lacătul. Un rol copiat de la
altcineva are fișa altcuiva, și se vede imediat în livrabile.

Orchestratorul e singurul pe care skill-ul nu îl construiește, de-aia e aici.

## Cum pornești

1. Clonează repo-ul și dă-i numele flotei tale. Folderul în care îl pui devine rădăcina
   flotei: orchestratorul și fiecare rol stau ca subfoldere ale lui, lângă `campanie/`.
2. Scrie în `orchestrator/roluri.txt` prefixele rolurilor tale, câte unul pe linie. Vin
   completate cu exemplul de marketing, le înlocuiești.
3. Completează locurile marcate cu `<...>` din `orchestrator/CLAUDE.md`, `USER.md`,
   `MEMORY.md` și `TOOLS.md`. Restul textului e mecanismul și merge așa cum e.
4. Pentru fiecare rol, creează folderul lui și rulează `onboarding-agent` în el. Citește
   înainte `docs/INSTALARE-AGENT.md`.
5. Adaptează numele de fișiere din `orchestrator/scripts/verifica_livrabil.py` la livrabilele
   flotei tale. Logica rămâne, numele se schimbă.
6. Deschide o sesiune în `orchestrator/` și cere-i apelul de prezență.

## Documentația

`docs/METODOLOGIE.md`, **citește-o prima.** Explică de ce modul atelier și modul flotă se
exclud, și de ce o sesiune pornită nu recitește fișierele pe care i le editezi sub ea.

`docs/INSTALARE-AGENT.md`, cum construiești un rol și la ce te uiți în întrebările pe care
ți le pune skill-ul.

`docs/SABLON-AGENT.md`, structura fișierelor unui rol, ca referință.

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
