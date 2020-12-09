import requests
from bs4 import BeautifulSoup
import re
import time
import random


sold_item_name = []
sold_prices = []
sold_dates = []
sold_times = []


def get_sold_listings():
    for i in range(1, 51):
        user_agent_list = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        ]
        sold_url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=playstation+5&_sacat=0&LH_Sold=1&LH_Complete=1_pgn%3D1&_ipg=200&_pgn={i}&rt=nc"
        user_agent = random.choice(user_agent_list)
        # Set the headers
        headers = {"User-Agent": user_agent}
        response = requests.get(sold_url, headers=headers)
        data = response.text
        soup = BeautifulSoup(data)
        time.sleep(1)
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


# print(len(listings))
# for listing in listings:
#     print(listing.text)


item_name = []
prices = []


# this was really illustrative of that fact that data is in a constant state of flux and is somewhat fragile. If we were not careful
# with how we executed these scraping functions we could accidentally delete the previous scrape and lose it forever
def get_new_listings():
    for i in range(1, 21):
        time.sleep(2)
        user_agent_list = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        ]
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=playstation+5&_sacat=0&_ipg=200&_pgn={i}"
        user_agent = random.choice(user_agent_list)
        # Set the headers
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)
        data = response.text
        soup = BeautifulSoup(data)

        r = requests.get(url)
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


def store_ebay_sold_data(name, price, filepath, time=None, date=None):
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


def store_new_ebay_data(name, price, filepath):
    # write new numbers to empty txt file using w and file.write
    with open(filepath, "w") as file:
        file.write("Listing Title,Price" + "\n")
        for i, item in enumerate(name):
            this_line = item.replace(",", " ") + "," + str(price[i]) + "\n"
            file.write(this_line)
        return


# get_sold_listings()
# store_ebay_sold_data(
#     sold_item_name, sold_prices, "data/sold_scrape_tuesday.csv", sold_times, sold_dates
# )
# get_new_listings()
# store_new_ebay_data(item_name, prices, "data/new_ebay_tues.csv")
