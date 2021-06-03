import requests
from bs4 import BeautifulSoup


def check_price():
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Defined"
    }

    response = requests.get("https://www.amazon.com/Ultrean-Airfryer-Programmable-Detachable-Anti-scratch/dp/B07FF117K7/ref=sr_1_4?dchild=1&keywords=air+fryer&qid=1622741516&sr=8-4", headers=headers)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    price = float(soup.find_all(name="span", class_="priceBlockBuyingPriceString")[0].getText().replace("$", ""))
    