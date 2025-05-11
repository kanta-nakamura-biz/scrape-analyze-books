import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ターゲットURL
base_url = 'http://books.toscrape.com/'

# データを格納するリスト
all_data = []

# User-Agentの設定
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# 最大再試行回数と待機時間（秒）
MAX_RETRIES = 3
RETRY_DELAY = 5

def fetch_page(url):
    for i in range(MAX_RETRIES + 1):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error during request to {url}: {e}")
            if i < MAX_RETRIES:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"Max retries exceeded for {url}. Skipping.")
                return None
    return None

# ページネーションされた書籍一覧ページを巡回する関数
def scrape_category_page(category_url, category):
    response = fetch_page(category_url)
    if response is None:
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    product_cards = soup.find_all('article', class_='product_pod')

    for card in product_cards:
        title_element = card.h3.a
        title = title_element['title']
        product_url_relative = title_element['href']
        product_url = base_url + 'catalogue/' + product_url_relative.replace('../../../', '')

        price_element = card.find('p', class_='price_color')
        price_str = price_element.text.replace('£', '')
        try:
            price = float(price_str)
        except ValueError as e:
            print(f"Error converting price: {price_str} on {product_url}. Error: {e}")
            price = None

        star_rating_classes = card.find('p', class_='star-rating')['class']
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating_str = [c for c in star_rating_classes if c != 'star-rating'][0]
        rating = rating_map.get(rating_str, None)

        if price is not None:
            all_data.append({
                'title': title,
                'product_url': product_url,
                'price': price,
                'rating': rating,
                'category': category
            })

    next_button = soup.find('li', class_='next')
    if next_button:
        next_page_relative_url = next_button.a['href']
        next_page_url = category_url.rsplit('/', 1)[0] + '/' + next_page_relative_url
        print(f"Scraping next page: {next_page_url}")
        time.sleep(1)
        scrape_category_page(next_page_url, category)

# 全てのカテゴリーのURLを取得してスクレイピングを開始する
response = fetch_page(base_url)
if response is None:
    print("Failed to retrieve the main page. Exiting.")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
category_links = soup.select('.side_categories li a')

for link in category_links[1:]:  # 最初の'Books'リンクは除く
    category_name = link.text.strip()
    category_relative_url = link['href']
    category_url = base_url + category_relative_url
    print(f"Scraping category: {category_name}")
    time.sleep(1)
    scrape_category_page(category_url, category_name)

# スクレイピングしたデータをPandas DataFrameに変換
df = pd.DataFrame(all_data)

# CSVファイルに保存
df.to_csv('books_data.csv', index=False, encoding='utf-8')
print("\nData saved to books_data.csv")