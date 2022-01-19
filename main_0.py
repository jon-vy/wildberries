import requests
from lxml import html

links_1_list = []
links_2_list = []
def get_url_0():
    r = requests.get('https://www.wildberries.ru')
    html_body = html.fromstring(r.text)
    links_0 = html_body.xpath("//ul[@class='menu-burger__main-list']/li/a[@href]")
    links_0_list = []
    # f = open('links.txt', 'w')
    for i in range(len(links_0)):
        # f.write(f"{links[i].attrib['href']}\n")
        links_0_list.append(links_0[i].attrib['href'])
        print(f"link_0 {i} | {links_0[i].attrib['href']}")
    return links_0_list

def get_url_1(link_0):
    # print(f"link_0 {link_0}")
    r = requests.get(link_0)
    html_body = html.fromstring(r.text)
    links_1 = html_body.xpath("//ul[@class='menu-catalog__list-2']/li/a[@href]")
    # print(f"links_1 {links_1}")

    for i in range(len(links_1)):
        links_1_list.append(f"https://www.wildberries.ru{links_1[i].attrib['href']}")
        print(f"link_1 {i} | {links_1[i].attrib['href']}")
    return links_1_list

def get_url_2(link_1):
    r = requests.get(link_1)
    # print(r)
    html_body = html.fromstring(r.text)
    links_2 = html_body.xpath("//li[@class='selected hasnochild']/ul/li/a[@href]")
    for i in range(len(links_2)):
        links_2_list.append(f"https://www.wildberries.ru{links_2[i].attrib['href']}")
        print(f"https://www.wildberries.ru{links_2[i].attrib['href']}")
    return links_2_list

if __name__ == '__main__':
    links_0_list = get_url_0()  # ссылки вида https://www.wildberries.ru/catalog/zhenshchinam


    for i in range(len(links_0_list)):
        link_0 = links_0_list[i]
        links_1_list = get_url_1(link_0)  # ссылки вида https://www.wildberries.ru/catalog/zhenshchinam/odezhda

    # for i in range(len(links_1_list)):
    #     print(f"link_1 {i} {links_1_list[i]}")

    for i in range(len(links_1_list)):
        link_1 = links_1_list[i]
        links_2_list = get_url_2(link_1)

    # for i in range(len(links_2_list)):
    #     print(f"link_2 {i} {links_2_list[i]}")
