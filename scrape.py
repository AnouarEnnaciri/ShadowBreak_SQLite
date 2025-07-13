import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import csv
import time
import random

options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)
driver.get("https://www.welovebuzz.com")
time.sleep(random.uniform(3, 5))

soup = BeautifulSoup(driver.page_source, "html.parser")
articles = soup.select("article")

with open("welovebuzz_articles.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])

    for article in articles:
        h2 = article.find("h2")
        a = h2.find("a") if h2 else None
        if a:
            title = a.get_text(strip=True)
            link = a['href']
            writer.writerow([title, link])
            print(f"[✓] {title} → {link}")

try:
    driver.quit()
except:
    pass
