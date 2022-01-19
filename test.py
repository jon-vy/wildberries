import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36'
}

URL = 'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki'  #?page=1

def pars_items():
    i = 1
    url_item_list = []
    while True:
        if len(url_item_list) < 1000:
            r = requests.get(URL, headers=HEADERS, params={'page': i})
            src = r.text
            soup = BeautifulSoup(src, "lxml")
            divs = soup.findAll("div", class_="product-card j-card-item")
            if len(divs) != 0:
                for div in divs:
                    id_item = div.attrs['data-popup-nm-id']
                    url_item_list.append(f"https://www.wildberries.ru/catalog/{id_item}/detail.aspx")
                    print(f"{len(url_item_list)} https://www.wildberries.ru/catalog/{id_item}/detail.aspx")
                i = i + 1
            else: break
        else: break  # спарсил 1000 товара и вышел из цикла
        # return url_item_list

def pars_item_data(url):
    pass

if __name__ == '__main__':
    url = 'https://www.wildberries.ru/catalog/40905699/detail.aspx'
    pars_item_data(url)