BookScraper is a simple Python project that scrapes book details (title, currency, and price) from books.toscrape.com using Requests and BeautifulSoup.
The scraped data is then saved as a clean, formatted JSON file.


Features

Scrapes book title, currency, and price
Clean JSON output
Uses requests for fetching and BeautifulSoup for parsing
Handles encoding properly
Beginner-friendly and easy to extend


Tech Stack

Python 3

Requests

BeautifulSoup (bs4)

JSON



How It Works

Send a GET request to the website

Parse the HTML using BeautifulSoup

Extract book data from each product card

Store results in a list

Save to books.json using json.dump()


Installation
1. Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. Install required packages
pip install requests beautifulsoup4



Run the script:

python scrape.py


Output Example

[
    {
        "title": "A Light in the Attic",
        "currency": "£",
        "price": 51.77
    },
    {
        "title": "Tipping the Velvet",
        "currency": "£",
        "price": 53.74
    }
]

Future Improvements

Save data to CSV

Store data in a database

Create a CLI tool or GUI

Add exception handling
