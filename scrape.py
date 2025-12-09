import requests
from bs4 import BeautifulSoup
import json
import csv
import sqlite3
url="https://books.toscrape.com/"
con = sqlite3.connect('students1.sqlite3')
cur = con.cursor()

def create_table():
    book_query="""
    create table book(
    id integer primary key autoincrement,
    title varchar not null,
    currency varchar not null,
    price varchar not null
    )
    """
    cur.execute(book_query)
    con.commit()

def insert_items(title, currency, price):
    insertion = """
    insert into book('title','currency','price') values (?,?,?)
    """
    
    cur.execute(insertion,(title, currency, price))
    con.commit()
    
def read_items():
    select = "select * from book"
    cur.execute(select)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def scarpe_books(url):
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
        
    return all_books



def json_file(all_books):
    with open("books.json","w",encoding="utf-8") as f:
        json.dump(all_books, f, indent=4, ensure_ascii=False)

def csv_file(all_books):
    headers = all_books[0].keys()
    with open("books.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_books[0].keys())
        writer.writeheader()
        writer.writerows(all_books) 

def separation(all_books):
    with open("discounted.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_books[0].keys())
        writer.writeheader()  # write only the column name once

        for i in all_books:
            if i["price"] < 40:
                writer.writerow(i)

            


        
def main():
    create_table()
    books = scarpe_books(url)
    for b in books:
        insert_items(b['title'], b['currency'], b['price'])
    
    json_file(books)
    csv_file(books)
    read_items()
    separation(books)

main()
