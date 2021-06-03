import requests
import smtplib
from bs4 import BeautifulSoup

user = "???"
password = "???"

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Defined"
}

url = "https://www.amazon.com/Ultrean-Airfryer-Programmable-Detachable-Anti-scratch/dp/B07FF117K7/ref=sr_1_4?dchild=1&keywords=air+fryer&qid=1622741516&sr=8-4"

response = requests.get(f"{url}", headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")

title_div = soup.find(name="div", class_="centerColAlign")
title = title_div.find(name="span", class_="product-title-word-break").getText().replace("\n\n\n\n\n\n\n\n", "").split(",")[0]

price = float(soup.find_all(name="span", class_="priceBlockBuyingPriceString")[0].getText().replace("$", ""))
target_price = 100

if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user, to_addrs="edwinzwa@hotmail.com", msg=f"Subject:Price Alert!!\n\nThe price of {title} is below ${target_price}!\n Buy Now: {url}")