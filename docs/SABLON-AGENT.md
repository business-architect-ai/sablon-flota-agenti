# Cele șase fișiere ale unui rol

Forma de completat e în `agent-sablon/`, nu aici. O copiezi în folderul rolului și completezi
locurile `<...>`. Documentul ăsta explică **la ce e fiecare fișier și ce greșeală face dacă e
scris prost**, ca să știi ce cauți când completezi.

Regula de peste tot: ce nu știi încă rămâne necompletat, nu umplut cu presupuneri. Un rol
construit pe presupuneri le aplică și nu-ți spune care sunt.

---

## `CLAUDE.md`

**Singurul fișier citit automat la pornire.** Restul există doar fiindcă el le cheamă. Dacă
scoți un fișier din lista de la început, fișierul acela devine mort: rămâne pe disc și nu se
citește niciodată.

Aici stau lanțul (de la cine primești, cui raportezi), protocolul de predare și limitele.

Greșeala tipică: pui aici și meseria, și purtarea, și limitele, și fișierul crește până nu
mai știi ce e regulă și ce e explicație. Meseria merge în `IDENTITY.md`, purtarea în
`SOUL.md`.

## `IDENTITY.md`

Cine e și pentru ce răspunde. **O singură responsabilitate, îngustă.**

Un rol care răspunde de tot nu răspunde de nimic, iar la prima nelămurire alege singur ce e
mai important, de obicei altfel decât ai fi vrut.

Secțiunea „de ce NU răspunzi" e la fel de importantă ca prima, și e cea pe care o sari.
Fără ea, rolul va face treaba vecinului „ca să meargă mai repede", iar atunci nu mai are cine
să verifice pe cine.

## `SOUL.md`

Cum lucrează. Aici e diferența dintre un rol generic și unul calibrat.

Scrie exemple, nu adjective. „Ton profesionist" nu înseamnă nimic executabil. „Scurt, spui ce
e gata și ce lipsește, fără progres estimat" înseamnă.

Aici stă și regula de adevăr: ce e dovedit, ce e presupus și ce lipsește stau separat. Fără
ea, un livrabil amestecă faptele cu deducțiile în același paragraf, iar cine citește nu poate
deosebi.

## `USER.md`

Pentru cine lucrează. Două lucruri diferite, amândouă contează: **omul** care îi dă de lucru
și **publicul** muncii.

Dacă livrabilul rolului merge la alt rol din flotă, atunci rolul acela e primul public, iar
omul al doilea. Asta schimbă ce înseamnă „bun": un fișier bun pentru om poate fi inutilizabil
pentru rolul următor.

## `TOOLS.md`

Ce unelte are și, mai important, ce n-are voie să atingă.

Greșeala care costă cel mai mult: fișierul se contrazice cu ce poate rolul în realitate. Un
`TOOLS.md` care spune „nu presupune că ai acces la internet" pe un rol care trebuie să citeze
surse de pe web îl pune să lucreze împotriva propriului fișier. La fel de rău e invers, un
fișier care promite unelte care nu există în sesiune.

Verifică în sesiune ce are, și scrie aia.

## `MEMORY.md`

Ce ține minte între porniri. **Gol e mai bine decât greșit.**

Se citește la fiecare pornire, deci o linie veche de aici costă mai mult decât oriunde
altundeva: rolul o aplică fără să o mai pună la îndoială.

Scrie regula, nu simptomul. Simptomele se schimbă odată cu mediul, și atunci fișierul devine
fals, nu doar vechi.

---

## Ce mai e în folderul unui rol

| Folder | Ce ține |
|---|---|
| `cunostinte/` | materiale citite la pornire, deci doar ce e folosit mereu |
| `memorie/` | un fișier pe subiect, ce rămâne adevărat între rulări |
| `ciorne/` | lucru în desfășurare, plus `sarcina.md` |

`ciorne/sarcina.md` merită explicat, fiindcă pare birocrație și nu e. Sarcina primită se
salvează acolo cuvânt cu cuvânt, înainte de orice altceva. E singurul fel în care se poate
verifica mai târziu dacă rolul a răspuns la tot ce s-a cerut, **fără să-l întrebi pe el**.
Dacă îl întrebi pe el, îți răspunde din ce-și amintește că a vrut să facă.

Și livrabilul se scrie în folderul comun **doar când e gata**. Un livrabil care se adună în
mai multe ture se lucrează în `ciorne/`, fiindcă orice apariție a fișierului în folderul comun
e tratată ca predare: orchestratorul vede un fișier care există și nu e gol, și pornește pasul
următor cu o ciornă.
