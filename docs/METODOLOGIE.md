# Metodologia de lucru în flotă

Pe același arbore de foldere se lucrează în două moduri care se exclud. Dacă nu le ții
separate, lucrurile par că merg și nu merg, iar depanarea e imposibilă, fiindcă nu știi ce
versiune a citit cine.

## De ce se exclud, pe scurt

**O sesiune pornită nu recitește fișierele.** Un agent citește `CLAUDE.md`, `IDENTITY.md`,
`SOUL.md`, `USER.md`, `MEMORY.md` și `cunostinte/` o singură dată, la pornire. Dacă îi
editezi un fișier în timp ce rulează, el lucrează în continuare cu ce a citit atunci. Nu
există reîncărcare și nu te anunță nimeni.

La asta se adaugă că `CLAUDE.md` din folderul părinte **cascadează** în toate subfolderele.
O editare la rădăcină atinge toți agenții, nu doar pe cel la care te gândeai.

## Cele două moduri

| | Mod atelier | Mod flotă |
|---|---|---|
| Ce deschizi | rădăcina flotei | fiecare agent în fereastra lui |
| Starea flotei | **oprită**, toate ferestrele de agent închise | pornită |
| Cine ești | arhitectul flotei | omul din fața orchestratorului |
| Ce ai voie să editezi | orice fișier, din orice agent | **nimic**, nici tu |
| Ce rulează | nimic | lanțul unei campanii |
| Ce iese | agenți mai buni | livrabile |

## Regula 1. Un mod pe sesiune de lucru, declarat la început

Niciodată amândouă în același timp. Restul regulilor decurg din asta.

Când ești în atelier și vrei să vezi dacă merge, închizi atelierul și treci în flotă.

Când ești în flotă și observi că un agent are o regulă prostească, **nu o repari pe loc.** O
notezi pe hârtie sau în memoria proiectului, termini lanțul, apoi treci în atelier. O reparație
făcută în mijlocul unui lanț nu ajunge la agentul care rulează, dar ajunge la următorul care
pornește, și atunci ai doi agenți care lucrează după reguli diferite.

## Regula 2. Trecerea din atelier în flotă trece prin repornire

Fără excepție, și în ordinea asta:

1. închizi **toate** ferestrele de agent, nu doar pe cea pe care ai editat-o, din cauza
   cascadei de la rădăcină
2. închizi fereastra rădăcinii
3. deschizi fiecare agent din nou, pe rând
4. ceri orchestratorului apelul de prezență
5. abia apoi dai prima sarcină

Pasul 4 nu e ceremonie. Apelul de prezență e singurul moment în care afli că un agent nu a
pornit, sau că ai două ferestre deschise pe același folder (`DUBLAT`), caz în care
orchestratorul nu trimite niciuneia și trebuie să închizi una.

## Regula 3. În modul flotă, fiecare scrie numai la el

Tu inclusiv. Dacă în timpul unui lanț deschizi `campanie/livrabile/copy.md` și corectezi o
virgulă, ai creat o versiune pe care copywriterul nu o cunoaște. La pasul următor, altcineva
citește fișierul tău și raportează despre textul lui.

Modificările de conținut le ceri agentului care a făcut treaba. El scrie, el te anunță, iar
orchestratorul cere refacerea pașilor care plecaseră din versiunea veche.

## Unde stă ce

| Ce | Unde | Citit de |
|---|---|---|
| arhitectura flotei: organigrama, contractul, șablonul | `README.md`, `SABLON-AGENT.md` | tine, în mod atelier |
| procedura de adăugare a unui agent | `INSTALARE-AGENT.md` | tine, în mod atelier |
| starea proiectului: ce s-a făcut, ce urmează | memoria proiectului rădăcină | tine, când deschizi rădăcina |
| meseria unui agent | cele șase fișiere din folderul lui | agentul, la pornire |
| livrabilele campaniei | `campanie/` | toți, după contract |

**La rădăcină nu există și nu are voie să existe `CLAUDE.md`.** Cascadează în fiecare agent și
intră peste persona lui. Contextul de arhitectură e pentru tine, nu pentru ei, deci stă în
`README.md` și în memoria proiectului, care nu cascadează.

## Fluxul stă într-un singur loc

Un agent răspunde la două întrebări diferite, care nu se amestecă:

- **cum lucrează**, adică pașii
- **când a terminat bine**, adică criteriile de acceptare

Fiecare întrebare are **un singur** răspuns pe disc. Unde stă, depinde de cât de complicat e
agentul:

| Situație | Cum lucrează | Când a terminat bine |
|---|---|---|
| o meserie, încape în zece rânduri | `CLAUDE.md` | `CLAUDE.md` (orchestratorul: „fișierul există și nu e gol") |
| o meserie, dar lungă | `FLUX.md` | `VERIFICARE.md` |
| mai multe meserii distincte | câte un skill | în fiecare skill, la pasul de verificare |

`FLUX.md` și `VERIFICARE.md` nu se bat cap în cap, răspund la cele două întrebări diferite,
și de-aia agenții din `onboarding-agent` le au pe amândouă.

**Contradicția apare între rândurile tabelului, nu în el.** Un agent care are și `FLUX.md`, și
skill-uri care descriu aceiași pași, are două instrucțiuni pentru aceeași treabă. Secțiunile
se suprapun unu la unu: „ce primești", „pașii", „verific înainte să livrez", „unde pun
rezultatul".

Și nu se depanează. Fișierele din lista de lectură se citesc la fiecare pornire, un skill doar
când se declanșează, deci agentul duce mereu versiunea generică și uneori primește deasupra pe
cea specifică. Când diferă, nu primești nicio eroare, primești un amestec, iar agentul
raportează că a terminat.

**Când un agent cu `FLUX.md` crește și capătă a doua meserie**, pașii lui se mută în primul
skill și `FLUX.md` se retrage. Criteriile din `VERIFICARE.md` se mută la pasul de verificare
al skill-ului. Nimic nu rămâne „ca referință".

## Semne că ai amestecat modurile

- un agent se purta corect ieri și azi ignoră o regulă pe care o vezi scrisă în fișierul lui:
  rulează de dinainte de editare, repornește-l
- doi agenți din același lanț lucrează după reguli diferite: unul a pornit înainte de o
  modificare la rădăcină, celălalt după
- orchestratorul spune că un agent lipsește, deși fereastra e deschisă: ori e `DUBLAT`, ori
  adresa s-a schimbat la repornire și trebuie rulat din nou `scripts/flota.sh`
- un livrabil are o modificare pe care niciun agent nu o revendică: ai editat tu în mod flotă
