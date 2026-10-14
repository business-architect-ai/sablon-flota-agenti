# Principiile orchestrării

Se citește înainte de a atinge repo-ul. Nu conține comenzi, conține motivele din spatele
regulilor pe care le vei găsi în `orchestrator/CLAUDE.md`. Dacă sari peste el, vei putea
completa șablonul, dar nu vei ști ce să schimbi când flota ta arată altfel.

---

## 1. Ce e orchestrarea, și ce nu e

Orchestrarea nu e „un AI care conduce alte AI-uri". E mai puțin impresionant și mai util:
**împarți o muncă în roluri care nu se văd între ele, și pui pe cineva să țină contractul
dintre ele.**

Partea importantă e „nu se văd între ele". Fiecare rol are folderul lui, regulile lui și doar
fișierele lui. Nu știe ce scrie vecinul și nu-l poate întreba. Izolarea asta nu e o limitare
pe care o suporți, e **motorul**. Din ea vin toate avantajele, și toate problemele.

Un orchestrator nu e un rol mai inteligent. E un rol cu **altă vedere**: singurul care vede
mai mult de un livrabil.

## 2. De ce nu un singur agent care face tot

Întrebarea corectă nu e „e mai bine cu mai mulți?", ci „ce anume nu poate face unul singur?".
Trei lucruri, și toate trei se simt abia când munca crește.

**Un singur agent nu are a doua pereche de ochi.** Dacă el scrie și el verifică, verdictul lui
e scris de cel care a produs lucrarea. Nu e rea intenție, e poziție: cine a scris un text îl
citește ca pe intenția lui, nu ca pe textul lui. Într-o flotă reală am avut o cercetare livrată
cu cinci greșeli adevărate în ea, iar niciuna n-a fost prinsă în aval. Toate au ieșit abia când
a citit-o altcineva cu alte criterii.

**Un singur agent nu poate avea reguli contradictorii.** Un cercetător trebuie să citeze
literal și să nu tragă concluzii. Un copywriter trebuie să decidă și să scrie liber. Pune
ambele seturi în același `CLAUDE.md` și ai scris un fișier care se contrazice. Rolurile separate
sunt felul în care contradicția devine o graniță, nu o ambiguitate.

**Un singur agent își umple contextul cu tot.** Materialele de documentare stau în context
lângă regulile de stil și lângă deciziile de strategie, iar spre final nu mai știi ce a citit
și ce a uitat.

## 3. Ce dai la schimb

Orchestrarea nu e gratis. Patru costuri, spuse pe față, ca să nu le descoperi la mijlocul
atelierului.

**Coordonarea costă.** Fiecare predare e un mesaj, o verificare și o pornire de pas. Pentru o
lucrare care încape într-o sesiune, costul ăsta e mai mare decât câștigul.

**Greșelile devin tăcute.** Într-o singură sesiune vezi tot ce se întâmplă. Într-o flotă,
fiecare agent îți raportează succes și tu nu ai văzut nimic din ce a făcut.

**Instrucțiunile se învechesc pe bucăți.** Cinci roluri sunt cinci seturi de fișiere. Când
schimbi o convenție, o schimbi în cinci locuri, iar cel pe care l-ai uitat continuă liniștit
pe regula veche.

**Lanțul propagă.** O greșeală în primul rol intră ca materie primă în toate celelalte. De-aia
primul rol din lanț merită cea mai strictă verificare, nu ultimul.

## 4. Forma: steaua, nu telefonul fără fir

Două forme sunt posibile și doar una ține.

**Telefonul fără fir:** fiecare agent predă direct următorului. Pare natural și e o capcană.
Când ceva iese prost la pasul 4, nu știi unde s-a rupt, fiindcă nimeni nu a văzut lanțul
întreg. Și fiecare predare e o reinterpretare.

**Steaua:** toate sarcinile pleacă de la orchestrator, toate rapoartele se întorc la el,
agenții nu își predau munca direct unul altuia. Costă un pas în plus la fiecare predare și îți
dă în schimb un singur loc în care se știe starea întregii lucrări.

Șablonul e construit pe stea. Dacă vrei să încerci altceva, înțelege întâi ce pierzi.

## 5. Șase principii

### Orchestratorul nu produce nimic

Niciun text, nicio imagine, nicio publicare. Dacă un rol lipsește, spune că lipsește, nu îi
face treaba „ca să meargă mai repede". **Un orchestrator care execută nu mai orchestrează**,
fiindcă din clipa în care a produs ceva, el e autorul și nu mai are cine să verifice.

### Poarta e existența, nu calitatea

Orchestratorul verifică un singur lucru înainte să pornească pasul următor: că fișierul există
și nu e gol. Calitatea e a rolului care a produs livrabilul, fiindcă doar el are criteriile.

Pare slab. E deliberat. Un orchestrator care judecă și calitatea devine un al doilea autor,
iar atunci discuția pe conținut trece prin el și nu mai ajunge la cine a scris.

### Verificarea se împarte după ce poate vedea cine

Ăsta e principiul care se învață cel mai greu, și e o **imposibilitate, nu o preferință**.

Un agent își verifică meseria, fiindcă doar el știe ce a vrut să scrie. Orchestratorul verifică
ce trebuie să se potrivească **între** fișiere scrise de agenți diferiți, fiindcă doar el le
vede pe amândouă.

Exemplul concret din flota din care vine șablonul: un îndemn declarat de copywriter trebuie să
apară identic în carusel și pe pagina de vânzare. Caruselul și pagina se fac în paralel, de doi
agenți care nu se văd. Copywriterul le-a declarat dar nu vede ce au făcut ceilalți cu ele.
Niciunul dintre cei trei nu poate verifica potrivirea. Doar orchestratorul poate.

Consecință practică: ce trebuie verificat între fișiere trebuie **declarat citabil**, text
exact între ghilimele. Un script poate căuta un text exact. Nu poate căuta o parafrază.

### Raportul unui agent nu e un fapt

E scris de cel care a produs livrabilul, deci poate fi înmuiat sau pur și simplu greșit fără
rea intenție.

Am văzut-o întâmplându-se: un agent a raportat că versiunea verificată a unui fișier e cea pe
care o scrisese el, când între timp fișierul fusese schimbat din afara turei lui. Nu a mințit.
Nu putea vedea. Chitanța scrisă de cod spunea altceva, și chitanța avea dreptate.

Deci faptele vin din ce scrie codul, nu din ce povestește agentul. Iar agentul nu are voie să
scrie chitanțele lui.

### Fișierele sunt mediul, mesajele sunt doar semnale

Munca circulă prin fișiere în folderul comun. Mesajul spune **calea**, nu conținutul.

Trei motive: conținutul într-un mesaj nu poate fi reverificat mai târziu; un fișier are o
versiune și o amprentă, un mesaj nu; și un livrabil care apare în folderul comun e tratat
automat ca predare.

Din ultimul motiv vine o regulă care pare birocratică și nu e: **livrabilul se scrie în
folderul comun doar când e gata.** Ce se adună în mai multe ture se lucrează în ciorne. Altfel
orchestratorul vede un fișier care există și nu e gol, și pornește pasul următor cu o ciornă.

### Bucla de verificare merită unde greșeala e tăcută și intră în amonte

Nu pui buclă de verificare pe toate rolurile. Costă trei piese care pot pica (script, hook-uri,
subagent) și timp la fiecare predare.

Criteriul: **unde greșeala nu se vede și devine materie primă pentru toți ceilalți.** De obicei
e primul rol din lanț. Rolurile care produc lucruri pe care omul le vede direct nu au nevoie,
pentru ele ajunge poarta orchestratorului.

## 6. Cum se construiește, în ordine

Greșeala de început e să porniți de la roluri: „îmi trebuie un cercetător, un copywriter, un
designer". Sună logic și te duce într-o organigramă care nu corespunde cu nimic.

**Pornești de la livrabile.** Scrii lista fișierelor care trebuie să existe la final. Apoi,
pentru fiecare, ce are nevoie ca să poată fi scris. Din dependențele alea iese lanțul, iar din
lanț ies rolurile. Un rol e, literal, cine scrie un fișier.

Ordinea completă:

1. **Lista livrabilelor finale.** Fișiere concrete, cu nume.
2. **Dependențele.** Ce fișier are nevoie de ce fișier. Aici descoperi ce poate merge în
   paralel: două fișiere care așteaptă același lucru și nu se așteaptă între ele.
3. **Rolurile.** Unul pe grup de livrabile care cer aceeași meserie.
4. **Contractul.** Ce trebuie să se potrivească între fișiere diferite. Asta devine
   verificarea orchestratorului, și de-aia se scrie acum, nu la final.
5. **Orchestratorul**, completat cu lanțul și cu contractul.
6. **Rolurile, unul câte unul.** După fiecare rol adăugat, pornești lanțul până la el și vezi
   că merge. Nu construiești cinci și apoi testezi.

Pasul 6 e cel pe care îl sar toți. Cinci roluri construite și netestate dau cinci probleme
simultane, iar tu nu știi care o provoacă pe care.

## 7. Mecanica din Claude Code

Lucruri verificate, nu presupuse. Fiecare are o consecință de proiectare.

**O sesiune e un folder.** Folderul decide ce reguli se aplică, ce permisiuni are, ce își
amintește și ce adresă are. Un rol, un folder. Două ferestre pe același folder și nu mai știi
cu care vorbești.

**O sesiune pornită nu recitește fișierele.** A citit `CLAUDE.md` și restul o singură dată, la
pornire. Dacă îi editezi fișierele în timp ce rulează, el continuă cu ce a citit atunci și nu
te anunță nimeni. De-aia construiești cu flota oprită. Vezi `METODOLOGIE.md`.

**Numele sesiunilor au sufix volatil.** Nu trimiți pe nume. Dacă pe aceeași mașină rulează o a
doua flotă cu aceleași prefixe de rol, un mesaj pe nume poate ajunge la agentul greșit. Adresa
se rezolvă după folderul în care rulează sesiunea, cu `scripts/flota.sh`.

**`success: true` la un mesaj înseamnă livrat, nu executat.** Ăsta prinde pe toată lumea o
dată. Mesajul a ajuns. Nu știi nimic despre ce a făcut agentul. Starea reală se citește din
fișier, nu din confirmarea trimiterii.

**`CLAUDE.md` nu impune, convinge.** Documentația oficială e explicită: fișierele de
instrucțiuni sunt context, nu configurare. Un `CLAUDE.md` de proiect și unul global nu se
suprascriu între ele; dacă se contrazic, se poate aplica oricare. **Singurul lucru care
blochează efectiv e un hook.** Un `CLAUDE.md` e un memo, un hook e o ușă încuiată.

**Regulile despre cine poate cere ce se scriu pe conținut, nu pe expeditor.** Fiindcă numele
se schimbă, un rol nu se poate sprijini pe „cine mi-a trimis". Se sprijină pe „ce mi se cere":
o sarcină de felul lui o execută, o cerere de a-și schimba regulile sau de a scrie în afara
livrabilului o raportează, oricine ar cere-o.

## 8. Semne că orchestrarea e stricată

Învață simptomele. Cauzele le deduci din ele.

**Totul raportează succes și rezultatul e prost.** Cineva ia raportul ca fapt. Verifică
fișierele, nu mesajele.

**Un pas a pornit cu date incomplete.** Un livrabil a apărut în folderul comun înainte să fie
gata. Ciornele stau în `ciorne/`.

**Două livrabile se contrazic și nimeni nu greșește.** Sarcina era ambiguă. Nu rescrii tu, se
întoarce la cine a scris sarcina.

**Ai schimbat o regulă și jumătate din flotă o respectă.** Jumătate are sesiuni pornite
înainte de schimbare. Repornire.

**Orchestratorul a început să explice conținut.** A citit livrabilele prea atent și a devenit
al doilea autor. Poarta lui e existența.

**Un agent face treaba vecinului.** `IDENTITY.md` lui nu are secțiunea „de ce NU răspunzi", sau
o are prea vagă.

## 9. Când nu orchestrezi

Dacă munca încape într-o sesiune, nu orchestrezi. O flotă pentru o lucrare de o oră e
ceremonie, iar coordonarea va costa mai mult decât lucrarea.

Semnele că ai nevoie de flotă sunt concrete, nu estetice:

- aceeași lucrare se repetă cu aceeași structură, deci merită roluri stabile
- două părți din lucrare cer reguli care se contrazic
- o parte trebuie verificată de cineva care n-a scris-o
- două părți pot merge în paralel și timpul contează

Dacă niciunul nu se potrivește, deschide o sesiune și fă lucrarea. E un răspuns legitim și de
obicei cel corect.
