Engeto Python akademie
Třetí projekt: Elections scraper

POPIS PROJEKTU
Projekt slouží k extrahování výsledků voleb do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. – 21.10.2017.

INSTALACE KNIHOVEN
Použité knihovny jsou součástí souboru requirements.txt.
Pro instalaci doporučuji spustit v novém virtuálním prostředí následovně:
pip install -r requirements.txt

SPUŠTĚNÍ PROJEKTU
Pro spuštění projektu jsou potřeba dva povinné argumenty ('odkaz_uzemniho_celku' a 'jmeno_souboru').
Poté se stáhne soubor s výsledky v .csv.

UKÁZKA PROJEKTU
Výsledky hlasování v okrese Liberec:
1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103
2. argument: vysledky_liberec.csv

Spuštění programu:
python election_scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103' 'vysledky_liberec.csv'

Průběh stahování:
STAHUJI DATA Z VYBRANÉHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103
UKLADAM DO SOUBORU: vysledky_liberec.csv
UKONCUJI election_scraper.py

Částečný výstup:
kod_obce,nazev_obce,volici_v_seznamu,vydane_obalky,platne_hlasy...
563901,Bílá,718,452,449,30,1,0,37,71,23,5,1,7,0,1,51,0,9,137,0,2,11,2,5,1,1,51,3
563919,Bílý Kostel nad Nisou,785,523,518,24,7,1,9,138,49,3,4,12,0,0,34,0,12,163,1,0,1,0,1,0,0,59,0