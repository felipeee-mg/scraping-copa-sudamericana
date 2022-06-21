from bs4 import BeautifulSoup
import requests
import pandas as pd

lista_equipos = list()
lista_anios = list()
promedio_edad = list()
valor_mercado = list()
promedio_valor_mercado = list()
cantidad_jugadores = list()
cantidad_jugadores_extranjeros = list()
paises = list()

for year in range(2020, 2009, -1):
    print(year)
    url = 'https://www.transfermarkt.es/copa-sudamericana/teilnehmer/pokalwettbewerb/CS/saison_id/{}'.format(year - 1)
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    div = soup.find('div', class_='responsive-table')
    tbody = div.find('tbody', class_='')
    equipos = tbody.find_all('td', class_='links no-border-links hauptlink')

    if year == 2016 or year == 2017:
        div = soup.find('div', class_='grid-view', id='yw2')
        tbody = div.find('tbody', class_='')
        equipos2 = tbody.find_all('td', class_='links no-border-links hauptlink')
        equipos = equipos + equipos2

    for equipo in equipos:
        lista_equipos.append(equipo.text)
        lista_anios.append(year)

        link = equipo.find('a', class_='', href=True)['href']
        equipo_id = link[link.rindex('/')+1:len(link)]
        equipo_nombre_url = link[1:link.find('/startseite')]

        url = 'https://www.transfermarkt.es/{}/kader/verein/{}/plus/0/galerie/0?saison_id={}'.format(equipo_nombre_url, equipo_id, year-1)
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(page.content, 'html.parser')

        div = soup.find('div', class_='row', id="verein_head")

        if equipo.text == 'CD El Nacional' or 'Deportivo Quito' or 'Fuerza Amarilla SC' or 'LDU de Loja':
            pais = 'Ecuador'
        elif equipo.text == 'Deportivo Capiatá' or 'CD Santaní' or 'Independiente FBC' or 'Club General Díaz de Luque' or 'Sportivo Luqueño' or 'Tacuary Football Club' or 'River Plate Asunción':
            pais = 'Paraguay'
        elif equipo.text == 'Sport Boys Warnes' or 'Club Universitario de Sucre' or 'GV Club Deportivo San José Oruro' or 'Real Potosí':
            pais = 'Bolivia'
        elif equipo.text == 'Deportivo Anzoátegui SC' or 'Deportivo Petare FC' or 'Deportivo Italia' or 'Llaneros de Guanare EF' or 'Yaracuyanos Fútbol Club' or 'Deportivo Anzoátegui SC' or 'Trujillanos FC':
            pais = 'Venezuela'
        elif equipo.text == 'CD León de Huánuco' or 'Rosario FC' or 'CD León de Huánuco':
            pais = 'Perú'
        elif equipo.text == 'Chiapas FC' or 'San Luis FC' or 'Tecos FC':
            pais = 'México'
        elif equipo.text == 'Joinville Esporte Clube (SC)' or 'Santa Cruz Futebol Clube (PE)' or 'Brasília Futebol Clube (DF)' or 'Criciúma Esporte Clube' or 'Associação Portuguesa de Desportos (SP) ' or 'Grêmio Barueri Futebol Ltda.' or 'Figueirense Futebol Clube':
            pais = 'Brasil'
        elif equipo.text == 'El Tanque Sisley' or 'Club Atlético Bella Vista':
            pais = 'Uruguay'
        else: pais = div.find('img', class_='flaggenrahmen')['title']

        print(equipo.text)
                
        if pais == 'Argentina':
            url = 'https://www.transfermarkt.es/{}/kader/verein/{}/plus/0/galerie/0?saison_id={}'.format(equipo_nombre_url, equipo_id, year)
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(page.content, 'html.parser')

        div = soup.find('div', class_='large-4 columns')
        tfoot = div.find('tfoot', class_='')
        valores = tfoot.find_all('td')


        if valores[2].text[valores[2].text.find(' '):] != ' mill. €' and valores[2].text != '-':
            valor_mercado.append((float(valores[2].text[0:valores[2].text.find(' ')].replace(',', '.')))/1000)
        elif valores[2].text == '-':
            valor_mercado.append(None)
        else:
            valor_mercado.append(float(valores[2].text[0:valores[2].text.find(' ')].replace(',', '.')))

        if valores[3].text[valores[3].text.find(' '):] != ' mill. €' and valores[3].text != '-':
            promedio_valor_mercado.append((float(valores[3].text[0:valores[3].text.find(' ')].replace(',', '.'))/1000))
        elif valores[3].text == '-':
            promedio_valor_mercado.append(None)
        else:
            promedio_valor_mercado.append(float(valores[3].text[0:valores[3].text.find(' ')].replace(',', '.')))

        promedio_edad.append(float(valores[1].text[0:valores[1].text.find(' ')].replace(',', '.')))


        div = soup.find('div', class_='large-8 columns')
        div2 = div.find('div', class_='responsive-table')
        tbody = div2.find('tbody')
        plantilla = tbody.find_all('tr', class_=['odd','even'])
        cantidad_jugadores.append(len(plantilla))

        extranjeros = 0
        for p in plantilla:
            if p.find('img', class_='flaggenrahmen')['title'] != pais:
                extranjeros = extranjeros + 1

        cantidad_jugadores_extranjeros.append(extranjeros)
        paises.append(pais)

pd.DataFrame({'equipo' : lista_equipos, 'edicion' : lista_anios, 'pais' : paises, 'valor_mercado' : valor_mercado, 'promedio_valor_mercado' : promedio_valor_mercado, 'promedio_edad' : promedio_edad, 'cantidad_jugadores' : cantidad_jugadores, 'cantidad_jugadores_extranjeros' : cantidad_jugadores_extranjeros}).to_csv('copa_sudamericana.csv', index=False)

