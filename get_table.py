from bs4 import BeautifulSoup
import pandas as pd


def new_soup_from_file(file):
    with open('index.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
    return soup


def new_soup_from_html_src(html_src):
    soup = BeautifulSoup(html_src, 'html.parser')
    return soup


def get_data(soup):
    table_e = soup.find('table', {"class": "tabela__equipes"})
    table_p = soup.find('table', {"class": "tabela__pontos"})

    data_e = {'posicao': [], 'equipe': []}
    data_p = {
        'pontos': [],
        'jogos': [],
        'vitorias': [],
        'empates': [],
        'derrotas': [],
        'gp': [],
        'gc': [],
        'sg': [],
        'aproveitamento %': [],
        'ultimos': []
    }

    for row_e in table_e.tbody.find_all('tr'):
        values_e = row_e.find_all('td')

        posicao = values_e[0].text
        equipe = values_e[1].text[:-3]

        data_e['posicao'].append(posicao)
        data_e['equipe'].append(equipe)

    for row_p in table_p.tbody.find_all('tr'):
        values_p = row_p.find_all('td')
        pontos = values_p[0].text
        jogos = values_p[1].text
        vitorias = values_p[2].text
        empates = values_p[3].text
        derrotas = values_p[4].text
        gp = values_p[5].text
        gc = values_p[6].text
        sg = values_p[7].text
        aproveitamento = values_p[8].text
        ultimos = []
        for x in values_p[9].contents:
            ultimos.append(x.get('class')[1][-1])

        data_p['pontos'].append(pontos)
        data_p['jogos'].append(jogos)
        data_p['vitorias'].append(vitorias)
        data_p['empates'].append(empates)
        data_p['derrotas'].append(derrotas)
        data_p['gp'].append(gp)
        data_p['gc'].append(gc)
        data_p['sg'].append(sg)
        data_p['aproveitamento %'].append(aproveitamento)
        data_p['ultimos'].append(ultimos)

    df_e = pd.DataFrame(data_e)
    df_p = pd.DataFrame(data_p)
    df = pd.concat([df_e, df_p], axis=1)

    return df
