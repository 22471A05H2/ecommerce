import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    """Fetch HTML content from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

def parse_products(html):
    """Parse product information from HTML using BeautifulSoup."""
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    # Example: Books to Scrape site
    product_cards = soup.find_all('article', class_='product_pod')

    for card in product_cards:
        name = card.h3.a['title']
        price_raw = card.find('p', class_='price_color').get_text(strip=True)
        
        # Convert £ to ₹
        price = price_raw.replace('£', '₹').strip()

        # Add rating stars
        rating_class = card.p['class'][1]
        rating = f"{rating_class} stars"

        # Add extra spaces for padding
        name_padded = f"  {name}  "
        price_padded = f"  {price}  "
        rating_padded = f"  {rating}  "

        products.append({
            'Name': name_padded,
            'Price': price_padded,
            'Rating': rating_padded
        })

    return products

def save_to_csv(data, filename):
    """Save product data to a CSV file with SR column."""
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['SR', 'Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for idx, item in enumerate(data, start=1):
            row = {
                'SR': idx,
                'Name': item['Name'],
                'Price': item['Price'],
                'Rating': item['Rating']
            }
            writer.writerow(row)

def main():
    url = 'https://books.toscrape.com/catalogue/category/books/science_22/index.html'
    print("Fetching page...")
    html = fetch_html(url)

    if html:
        print("Parsing products...")
        products = parse_products(html)

        if products:
            print(f"Found {len(products)} products. Saving to CSV...")
            save_to_csv(products, 'products.csv')
            print("✅ Data saved to products.csv")
        else:
            print("No products found.")
    else:
        print("Could not get HTML content.")

if __name__ == "__main__":
    main()
