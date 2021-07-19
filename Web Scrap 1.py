from bs4 import BeautifulSoup
import requests
import pandas as pd

shop_listId = []
shop_listName = []
shop_listCat = []
shop_listFloor = []
shop_listInfo = []

pageNum = 1
def find_shops():
    html_text = requests.get(f"https://aeonmall-bsdcity.com/shopping.php?page={pageNum}").text
    soup = BeautifulSoup(html_text, 'lxml')
    shops = soup.find_all('div', class_='list-shopping')
    for shop in shops:
        shop_name = shop.find('div', class_='desc-shopping').h3.text
        shop_category = shop.find('div', class_='desc-shopping').span.text
        shop_floor = shop.find('div', class_='tmaps').text
        shop_info = shop.find('div', class_='desc-shopping').a['href']

        shop_listId.append(shop_info[23:28])
        shop_listName.append(shop_name)
        shop_listCat.append(shop_category)
        shop_listFloor.append(shop_floor)
        shop_listInfo.append(f"https://aeonmall-bsdcity.com/{shop_info}")

while pageNum < 20:
    find_shops()
    if pageNum == 19:
        break
    pageNum += 1

df = pd.DataFrame(list(zip(shop_listId, shop_listName, shop_listCat, shop_listFloor, shop_listInfo)),
                  columns=['Id', 'Name', 'Category', 'Floor', 'Web'])

df.to_csv (r'E:\ProgramData\pythonProject\export_dataframe_aeonmall-bsdcity.csv', index=False, header=True)