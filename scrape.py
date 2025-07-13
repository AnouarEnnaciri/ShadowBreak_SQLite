import requests
from bs4 import BeautifulSoup
import sqlite3

# Setup DB
conn = sqlite3.connect("articles.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    title TEXT,
    url TEXT UNIQUE
)
""")
conn.commit()

# Scrape
url = "https://www.welovebuzz.com/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("h2 a")  # Adjust this if needed

count = 0
for a in articles:
    title = a.get_text(strip=True)
    link = a.get("href")

    if title and link:
        try:
            cursor.execute("INSERT INTO articles (title, url) VALUES (?, ?)", (title, link))
            count += 1
        except sqlite3.IntegrityError:
            continue  # Skip duplicates

conn.commit()
conn.close()

print(f"✅ Scraped and inserted {count} new articles into articles.db")
