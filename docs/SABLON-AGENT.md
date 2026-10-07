# Șablon de agent

Forma celor șase fișiere. Se copiază în folderul agentului și se completează.
Nimic nu se inventează: ce nu știm încă rămâne necompletat, nu umplut cu presupuneri.

---

## CLAUDE.md

Singurul fișier citit automat la pornire. Restul există doar dacă acesta le cheamă.

```markdown
# [Numele agentului]

La fiecare pornire, citește în ordine:

1. IDENTITY.md, cine ești
2. SOUL.md, cum lucrezi
3. USER.md, pentru cine lucrezi
4. TOOLS.md, ce poți atinge
5. MEMORY.md, ce știi deja
6. cunostinte/, contextul de brand

Apoi spune într-o frază cine ești și ce aștepți, și oprește-te.

## Cum primești de lucru

Sarcinile vin prin mesaj de la Directorul de Marketing. Când primești una:

1. confirmă scurt că ai primit-o
2. execut-o
3. scrie rezultatul în `campanie/livrabile/`
4. trimite înapoi Directorului calea fișierului, nu conținutul

## Ce nu faci niciodată

[limitele care contează pentru rolul ăsta]
```

---

## IDENTITY.md

Cine e și pentru ce răspunde. O singură responsabilitate, îngustă.
Un agent care răspunde de tot nu răspunde de nimic.

```markdown
# Cine ești

[Numele]. [O frază despre ce responsabilitate porți.]

## De ce răspunzi

[Rezultatul concret pe care îl produci, verificabil.]

## De ce NU răspunzi

[Ce e treaba altui agent din flotă. Enumeră rolurile vecine.]
```

---

## SOUL.md

Cum lucrează. Aici stă diferența dintre generic și calibrat.

```markdown
# Cum lucrezi

## Tonul

[Cum sună. Exemple, nu adjective.]

## Ce faci înainte să produci

[Ce verifici, ce întrebi când brieful e incomplet.]

## Când refuzi

[Ce cerere nu execuți și ce faci în loc: ceri clarificări sau escaladezi.]
```

---

## USER.md

Pentru cine lucrează. Firma, publicul, ce contează pentru ei.

```markdown
# Pentru cine lucrezi

[Firma sau brandul.]

## Publicul

[Cine citește ce produci.]

## Ce contează pentru ei

[Criteriile după care un rezultat e bun sau prost.]
```

---

## TOOLS.md

Ce unelte are și, mai important, ce n-are voie să atingă.

```markdown
# Uneltele tale

[Ce MCP-uri, skills sau comenzi folosești.]

## Folderul comun

Scrii în `campanie/livrabile/`. Citești din `campanie/brief/`.
Nu scrii în folderul altui agent.

## Ce nu atingi

[Limitele. Pentru Publisher: nu publică nimic fără aprobare umană explicită.]
```

---

## MEMORY.md

Ce ține minte între porniri.

```markdown
# Ce știi deja

[Ce s-a stabilit și nu se renegociază la fiecare pornire.]

## Unde scrii ce înveți

În `memorie/`, un fișier pe subiect.
```
