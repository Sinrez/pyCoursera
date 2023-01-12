import requests
from bs4 import BeautifulSoup


index_page_url = "https://parsinger.ru/html/index1_page_1.html"

index_page_response = requests.get(index_page_url)
index_page_response.encoding = "utf-8"
index_page_soup = BeautifulSoup(index_page_response.text, 'html.parser')

schema = "https://parsinger.ru/html/"
all_categories_links = [tag["href"] for tag in index_page_soup.find("div", class_="nav_menu").find_all("a")]
all_category_pagination_links = []
for category_link in all_categories_links:
    category_page_response = requests.get(f"{schema}{category_link}")
    category_page_response.encoding = "utf-8"
    category_page_soup = BeautifulSoup(category_page_response.text, 'html.parser')
    all_category_pagination_links.append([tag["href"] for tag in category_page_soup.find('div', class_='pagen').find_all("a")])

all_product_links = []
for category_pagination_links in all_category_pagination_links:
    for page_link in category_pagination_links:
        page_response = requests.get(f"{schema}{page_link}")
        page_response.encoding = "utf-8"
        page_soup = BeautifulSoup(page_response.text, "html.parser")
        all_products_cards = page_soup.find("div", class_="item_card")
        all_product_links.append([a_tag["href"] for a_tag in all_products_cards.find_all("a", class_="name_item")])


sum_of_all_price = 0
for products_links in all_product_links:
    for product_link in products_links:
        product_page_response = requests.get(f"{schema}{product_link}")
        product_page_response.encoding = "utf-8"
        product_page_soup = BeautifulSoup(product_page_response.text, "html.parser")
        in_stock_amount = int(product_page_soup.find("span", id="in_stock").text.split()[2])
        price = int(product_page_soup.find("span", id="price").text.split()[0])
        sum_of_all_price += in_stock_amount * price

print(sum_of_all_price)