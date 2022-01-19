import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36'
}

# with open('data/link_category_level_2.txt', 'r', encoding='utf-8') as f:
#     links_list = f.read().split('\n')
# url = links_list[0]

def pars(url):
    print(url)
    i = 1
    url_item_list = []
    while True:
        print(f"Страница каталога https://www.wildberries.ru/catalog/zhenshchinam/odezhda?page={i}")
        r = requests.get(url, headers=headers, params={'page':i})
        src = r.text
        soup = BeautifulSoup(src, "lxml")
        divs = soup.findAll("div", class_="product-card j-card-item")
        if len(divs) != 0:
            for div in divs:
                id_item = div.attrs['data-popup-nm-id']
                url_item_list.append(f"https://www.wildberries.ru/catalog/{id_item}/detail.aspx")
                print(f"https://www.wildberries.ru/catalog/{id_item}/detail.aspx")
            i = i + 1
        else: break
    return url_item_list



    # print(len(id_list))

# for link in links_list[:1]:
#     print(link)

if __name__ == '__main__':
    url = links_list[0]
    pars(url)
