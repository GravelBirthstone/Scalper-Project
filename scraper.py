import requests
from bs4 import BeautifulSoup
import numpy as np
from scipy import stats
import pandas as pd
import re


item_name = []
prices = []

for i in range(1, 10):

    ebayUrl = (
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=playstation+5&_sacat=0_pgn="
        + str(i)
    )
    r = requests.get(ebayUrl)
    data = r.text
    soup = BeautifulSoup(data)

    listings = soup.find_all("li", attrs={"class": "s-item"})

    for listing in listings:
        prod_name = " "
        prod_price = " "
        for name in listing.find_all("h3", attrs={"class": "s-item__title"}):
            if str(name.find(text=True, recursive=False)) != "None":
                prod_name = str(name.find(text=True, recursive=False))
                item_name.append(prod_name)

        if prod_name != " ":
            price = listing.find("span", attrs={"class": "s-item__price"})
            prod_price = str(price.find(text=True, recursive=False))
            prod_price = float(re.sub(",", "", prod_price.split("$")[1]))
            prices.append(prod_price)


def store_ebay_data(name, price):
    # write new numbers to empty txt file using w and file.write
    with open("data/ebay_data_tuesday.csv", "w") as file:
        file.write("Listing Title,Price" + "\n")
        for i, item in enumerate(name):
            this_line = item.replace(",", " ") + "," + str(price[i]) + "\n"
            file.write(this_line)
        return


# data_ps5 = pd.DataFrame({"Listing Title": item_name, "Prices": prices})
# print(data_ps5)
store_ebay_data(item_name, prices)
