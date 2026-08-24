import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_books_under_20():
    base_url = "https://books.toscrape.com/catalogue/"
    current_page_url = "https://books.toscrape.com/catalogue/page-1.html"
    results = []

    while current_page_url:
        print(f"Scraping: {current_page_url}")
        response = requests.get(current_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            # 1. Filter by price on the main card
            price_text = book.find('p', class_='price_color').text
            price_val = str(price_text.replace('£', ''))
            
            if price_val < 20.0:
                # 2. Get basic info
                title = book.h3.a['title']
                rel_link = book.h3.a['href']
                # Handle relative URLs correctly
                detail_url = base_url + rel_link.replace('../../../', '').replace('catalogue/', '')
                
                # 3. Visit detail page for UPC and Description
                detail_resp = requests.get(detail_url)
                detail_soup = BeautifulSoup(detail_resp.text, 'html.parser')
                
                # Extract UPC from table
                upc = detail_soup.find('th', string='UPC').find_next_sibling('td').text
                # Extract Availability
                availability = detail_soup.find('th', string='Availability').find_next_sibling('td').text
                # Extract Description (usually the first <p> that doesn't have a class after the ID "product_description")
                desc_tag = detail_soup.find('div', id='product_description')
                description = desc_tag.find_next_sibling('p').text if desc_tag else "No description"
                
                # Extract Star Rating
                rating_class = book.find('p', class_='star-rating')['class'][1]
                
                results.append({
                    'title': title,
                    'price': price_val,
                    'availability': availability,
                    'star_rating': rating_class,
                    'upc': upc,
                    'description': description,
                    'url': detail_url
                })
                
                # Respectful scraping delay
                time.sleep(0.1)

        # 4. Handle Pagination
        next_btn = soup.find('li', class_='next')
        if next_btn:
            next_page_path = next_btn.a['href']
            current_page_url = base_url + next_page_path
        else:
            current_page_url = None # Exit loop

    # 5. Export to CSV
    df = pd.DataFrame(results)
    df.to_csv('books_under_20.csv', index=False)
    print("Scrape complete. Saved to books_under_20.csv")

if __name__ == "__main__":
    scrape_books_under_20()