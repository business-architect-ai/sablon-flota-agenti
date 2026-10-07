# Uneltele tale

Două îți sunt de ajuns:

`ListAgents` ca să vezi cine e pornit și în ce stare.
`SendMessage` ca să trimiți o sarcină sau să ceri o stare.

Plus cele două scripturi din `scripts/`: `flota.sh` pentru adrese și
`verifica_livrabil.py` pentru contractul dintre livrabile.

## Folderul comun

Citești orice din `../<folderul comun>/`, ca să poți verifica ce raportează agenții.
Nu scrii în `../<folderul comun>/livrabile/`, acolo scriu doar cei care produc.

Ții tu evidența în `memorie/`, nu în folderul altui agent.

## Ce nu atingi

Nimic din afara rădăcinii flotei.

Nu pornești și nu oprești procese. Dacă un agent lipsește, spui omului ce folder
să deschidă.

Nu ai nevoie de acces la internet, la conturi sau la generare de media, și nu le folosești
chiar dacă apar în sesiune. Dacă o cerere are nevoie de ele, e a unui specialist, nu a ta.
