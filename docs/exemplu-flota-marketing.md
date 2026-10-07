# Exemplu: o flotă de marketing completată

Flota din care e extras șablonul. Cinci roluri, lanț de patru pași, folder comun `campanie/`.
E dată ca să vezi cum arată locurile `<...>` completate, nu ca să o copiezi.

## Rolurile

`orchestrator/roluri.txt`:

    research-strategie
    director-marketing
    copywriter
    creator-carusele
    web-designer

| Rol | Prefix |
|---|---|
| Research și Strategie | `research-strategie` |
| Director de Marketing | `director-marketing` |
| Copywriter | `copywriter` |
| Creator de carusele | `creator-carusele` |
| Web Designer | `web-designer` |

Un al șaselea rol, Publisher-ul, există ca folder dar nu intră la apelul de prezență: nu
există pas de publicare până nu decide omul altfel. E un exemplu util de rol construit și
ținut deliberat în afara lanțului.

## Lanțul

| Pas | Cui dai sarcina | Ce așteaptă înainte | Ce produce |
|---|---|---|---|
| 1 | Research și Strategie | brieful omului în `../campanie/brief/` | `livrabile/research.md` |
| 2 | Director de Marketing | research-ul | `strategie/brief-uri.md` și restul strategiei |
| 3 | Copywriter | brief-urile | `livrabile/copy.md` |
| 4a | Creator de carusele | copy-ul | `livrabile/carusel.md`, `livrabile/carusel/slide-N.png`, plus `livrabile/postari.md` și `livrabile/postari/` |
| 4b | Web Designer | copy-ul | `livrabile/landing.md`, `livrabile/directie-vizuala.md`, `livrabile/landing/index.html`, cu fotografiile în `livrabile/landing/imagini/` |

Pașii 4a și 4b pleacă în același timp: amândoi așteaptă `livrabile/copy.md` și niciunul nu
are nevoie de ce face celălalt.

## Ce verifică orchestratorul aici

Contractul, nu calitatea. Concret, în flota asta: că fiecare îndemn declarat în `copy.md`
apare cuvânt cu cuvânt în piesa lui, și igiena textului care ajunge la public.

De ce nu poate face asta niciun agent: îndemnul din carusel față de cel de pe pagină stă în
două fișiere scrise de doi agenți diferiți, în paralel. Copywriterul le-a declarat, dar nu
vede ce au făcut ceilalți cu ele. Creatorul vede doar caruselul. Web Designerul doar pagina.

De-aia declarația din `copy.md` trebuie să fie **citabilă**, text între ghilimele, nu o
descriere a îndemnului. Un script poate căuta un text exact; nu poate căuta o parafrază.

## Un rol cu buclă și unul fără

În flota asta, `research-strategie` are buclă proprie de verificare (script, evaluator,
lacăt, chitanțe), iar celelalte patru nu. Orchestratorul tratează diferit cele două cazuri,
după regula din `orchestrator/CLAUDE.md`, secțiunea „Flota e mixtă".

Alegerea n-a fost întâmplătoare. Research-ul e primul din lanț, iar o cifră inventată acolo
apare ca fapt în copy, în carusele și pe pagină, fără ca nimeni să mai verifice. Celelalte
roluri produc lucruri pe care omul le vede direct, deci scriptul de contract ajunge.

Criteriul, dacă vrei să-l aplici la flota ta: **bucla merită acolo unde greșeala e tăcută și
intră în amonte.**

## Intrările care vin de la om

`campanie/brief/`, cererea lui.
`campanie/brand/`, fișa de voce și fișa de vizual ale campaniei.

Dacă fișele de brand lipsesc, agentul care ajunge la un criteriu de voce sau de vizual se
oprește și cere. Nu e defecțiune, e comportamentul corect.
