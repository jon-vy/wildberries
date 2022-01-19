import requests
from bs4 import BeautifulSoup
url = 'https://www.wildberries.ru/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36'
}
def get_category_1():
    # r = requests.get(url, headers=headers)
    # src = r.text

    # f = open('data/get_category_1.html', 'w', encoding='utf-8')
    # f.write(r.text)

    file = open('data/get_category_1.html', 'r', encoding='utf-8')
    src = file.read()

    soup = BeautifulSoup(src, "lxml")
    li_list = soup.find("ul", class_="menu-burger__main-list").findAll("li")
    link_list = []
    f = open('data/link_category_level_1.txt', 'w', encoding='utf-8')
    for i in range(24):
        a = li_list[i].find("a").get("href")
        link_list.append(a)
        f.write(a + "\n")

    return link_list

if __name__ == '__main__':
    get_category_1()