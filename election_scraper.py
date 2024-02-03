"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Alžběta Karolyiová
email: akarolyiova@gmail.com
discord: betykar
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys


def election_scraper(odkaz_uzemniho_celku, jmeno_souboru):
    # získání obsahu webu
    response = requests.get(odkaz_uzemniho_celku)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'STAHUJI DATA Z VYBRANÉHO URL: {odkaz_uzemniho_celku}')

    # extrakce dat
    data_list = []
    for td_cislo, td_name in zip(
        soup.find_all('td', class_='cislo'),
        soup.find_all('td', class_='overflow_name')
    ):

        kod_obce = td_cislo.text.strip()
        nazev_obce = td_name.text.strip()

        # odkaz na detailní informace o obci
        link = td_cislo.find('a')
        if link:
            detailni_link = link.get('href')
            detailni_url = f'https://volby.cz/pls/ps2017nss/{detailni_link}'

            # požadavek na detailní stránku obce
            response_detail = requests.get(detailni_url)
            soup_detail = BeautifulSoup(response_detail.text, 'html.parser')

            volici_v_seznamu = soup_detail.find('td', {'headers': 'sa2'})\
                .text.strip()
            vydane_obalky = soup_detail.find('td', {'headers': 'sa3'})\
                .text.strip()
            platne_hlasy = soup_detail.find('td', {'headers': 'sa6'})\
                .text.strip()
            strany_list = []
            strany = soup_detail.find_all('td', class_='overflow_name')
            for strana in strany:
                strany_list.append(strana.text.strip())
            hlasy_dle_stran = {}
            for strana_nazev in strany_list:
                hlasy = soup_detail.find('td', string=strana_nazev)\
                    .find_next('td')
                hlasy_dle_stran[strana_nazev] = hlasy.text.strip()
            # přidání dat do seznamu
            data_list.append({
                'kod_obce': kod_obce,
                'nazev_obce': nazev_obce,
                'volici_v_seznamu': volici_v_seznamu,
                'vydane_obalky': vydane_obalky,
                'platne_hlasy': platne_hlasy,
                **hlasy_dle_stran
                })

    # uložení dat do CSV souboru
    fieldnames = [
        'kod_obce', 'nazev_obce', 'volici_v_seznamu', 'vydane_obalky',
        'platne_hlasy'
        ]
    fieldnames.extend(strany_list)

    with open(jmeno_souboru, mode='w', newline='', encoding='utf-8-sig') \
            as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        # zápis hlavičky CSV souboru
        writer.writeheader()

        # zápis dat
        for data in data_list:
            writer.writerow(data)
    print(f'UKLADAM DO SOUBORU: {jmeno_souboru}\n'
          f'UKONCUJI election_scraper.py')


# použití funkce
try:
    url_volby = sys.argv[1]
    soubor_volby = sys.argv[2]

    election_scraper(url_volby, soubor_volby)
except IndexError:
    print('Zadali jste málo argumentů.')
    exit
except UnboundLocalError:
    print('Zadaný url není funkční.')
    exit
