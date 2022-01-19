from category_1 import get_category_1
from category_2 import get_category_2
from parser import pars


links_2 = []
link_item_list = []
link_1 = get_category_1()

for url in link_1:
    print(url)
    link_2 = get_category_2(url)
    links_2.extend(link_2)
    print(link_2)

for url_2 in link_2:
    urls = pars(url_2)
    link_item_list.extend(urls)


# f = open('data/link_category_level_2.txt', 'w', encoding='utf-8')
# for link in links_2:
#     f.write(link + "\n")
# f.close()