import requests
from bs4 import BeautifulSoup
import json
url="https://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if(response.status_code != 200):
        print(f"failed to fetch!Status code {response.status_code}")
        return
    
    #set encoding explicitly to handle special characters correctly
    response.encoding = response.apparent_encoding
    
    
    soup = BeautifulSoup(response.text, "html.parser")
    books=soup.find_all("article", class_="product_pod")
    all_books=[]
    for book in books:
        title = book.h3.a['title'] #if we are using tag use . if attribute then big bracket
        price_text = book.find("p", class_="price_color").text
        # print(price_text, type(price_text))

        
        currency = price_text[0]
        price = float(price_text[1:])
        # print(title, currency, price)
        
        
        book_data = {
            "title": title,
            "currency": currency,
            "price": price,
            
        }
        all_books.append(book_data)
        
        json_data = json.dumps(all_books, indent=4)
        print(json_data)
        
        # print(all_books)
        
        with open("books.json","w") as f:
            json.dump(all_books, f, indent=4)


   
scrape_books(url)