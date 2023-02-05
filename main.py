import get_table
import get_html

url = "https://ge.globo.com/futebol/brasileirao-serie-a/"

if __name__ == '__main__':
    # html_src = get_html.get_html_src(url)
    # soup = get_table.new_soup_from_html_src(html_src)
    soup = get_table.new_soup_from_file('index')
    table = get_table.get_data(soup)
    print(table)
