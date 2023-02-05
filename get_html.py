from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def get_html_src(url):
    chrome_options = Options()
    # Opens the browser up in background
    chrome_options.add_argument("--headless")
    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        html_src = browser.page_source
    return html_src


def create_html_file(html_src, filename='index'):
    with open(f'{filename}.html', 'w', encoding='utf-8') as f:
        f.write(html_src)
