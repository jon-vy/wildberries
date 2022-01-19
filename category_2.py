import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36'
}

def get_category_2(link):
    # print(link)
    r = requests.get(link, headers=headers)
    src = r.text

    # f = open('data/get_category_2.html', 'w', encoding='utf-8')
    # f.write(r.text)

    # file = open('data/get_category_2.html', 'r', encoding='utf-8')
    # src = file.read()

    soup = BeautifulSoup(src, "lxml")
    try:
        li_list = soup.find("ul", class_="menu-catalog__list-2").findAll("li")
    except:
        li_list = soup.findAll("li", class_="menu-catalog-second__drop-item")
    # print(li_list)
    link_list = []
    for i in range(len(li_list)):
        a = li_list[i].find("a").get("href")
        # print(f"{i} {a}")
        link_list.append(f"https://www.wildberries.ru{a}")
    return link_list