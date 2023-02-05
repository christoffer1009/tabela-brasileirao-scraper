import get_table
import get_html

url = "https://ge.globo.com/futebol/brasileirao-serie-a/"

if __name__ == '__main__':
    # a partir do código fonte do site, usa selenium, pois o site é dinâmico e requests simples não retornam a tabela, mais lento
    html_src = get_html.get_html_src(url)
    soup = get_table.new_soup_from_html_src(html_src)
    
    # a partir de arquivo html local
    # html_src = get_html.create_html_file(url)
    # soup = get_table.new_soup_from_file('index')
    
    # constrói a tabela
    table = get_table.get_data(soup)
    print(table)
