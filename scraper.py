import requests
from bs4 import BeautifulSoup
import re
import time

item_name = []
prices = []

# this was really illustrative of that fact that data is in a constant state of flux and is somewhat fragile. If we were not careful
# with how we executed these scraping functions we could accidentally delete the previous scrape and lose it forever
def get_new_listings():
    for i in range(1, 20):

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


sold_item_name = []
sold_prices = []
sold_dates = []
sold_times = []


def get_sold_listings():
    sold_ebay_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=playstation+5&_sacat=0&LH_Sold=1&LH_Complete=1_pgn%3D1&_ipg=200&_pgn=1&rt=nc"
    for i in range(1, 2):
        time.sleep(1)

        # sold_ebay_url = (
        #     "https://www.ebay.com/sch/i.html?_from=R40&_nkw=playstation+5&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1_pgn%3D1&_ipg=200&_pgn="
        #     + str(i)
        # )
        r = requests.get(sold_ebay_url)
        data = r.text
        soup = BeautifulSoup(data)

        listings = soup.find_all("li", attrs={"class": "s-item"})
        for listing in listings:
            prod_name = " "
            prod_sold = " "
            sold_date = " "
            sold_time = " "
            for name in listing.find_all("h3", attrs={"class": "s-item__title"}):
                if str(name.find(text=True, recursive=False)) != "None":
                    prod_name = str(name.find(text=True, recursive=False))
                    sold_item_name.append(prod_name)
            if prod_name != " ":
                date = listing.find(
                    "span", attrs={"s-item__ended-date s-item__endedDate"}
                )
                sold_date = str(date.find(text=True, recursive=False))
                sold_time = str(date.find(text=True, recursive=False))
                sold_date = str(re.sub("-", "-", sold_date.split(" ")[0]))
                sold_time = str(re.sub("-", "-", sold_time.split(" ")[1]))
                sold_times.append(sold_time)
                sold_dates.append(sold_date)
                price = listing.find("span", attrs={"class": "s-item__price"})
                # if item price has children
                if price.contents:
                    price_sold = price.contents[0]
                    prod_sold = str(price_sold.find(text=True, recursive=False))
                    prod_sold = float(re.sub(",", "", prod_sold.split("$")[1]))
                    sold_prices.append(prod_sold)


# seperation of concerns


def store_ebay_data(name, price, filepath, time, date=None):
    # write new numbers to empty txt file using w and file.write
    with open(filepath, "w") as file:
        file.write("Listing Title,Price,Date,Time" + "\n")
        for i, item in enumerate(name):
            this_line = (
                item.replace(",", " ")
                + ","
                + str(price[i])
                + ","
                + str(date[i])
                + ","
                + str(time[i])
                + "\n"
            )
            file.write(this_line)
        return


get_sold_listings()
store_ebay_data(
    sold_item_name, sold_prices, "data/sold_scrape_tuesday.csv", sold_times, sold_dates
)
# get_new_listings()
# store_ebay_data(item_name, prices, "test_new.csv")
