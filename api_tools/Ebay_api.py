# https://www.youtube.com/watch?v=O5KdYrD6_H4
from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

keyword = input("Sony Playstation 5 Console")
api = finding(appid = "AlexPena-ScalperA-PRD-8f78bdb73-caeda5cc", config_file=None) 
api_request = {"keywords" :keyword, "outputSelector": "SellerInfo"}

response = api.execute("findItemsByKeywords", api_request)
soup = BeautifulSoup(response.content, "xml")
totalentries = int(soup.find("totalentries").text)
items = soup.find_all("items")
input(items[0])


# Finding API has recently been depreciated and completed item are no longer accepted.
# https://developer.ebay.com/signin?return_to=%2Fmy%2Fkeys
# https://developer.ebay.com/api-docs/buy/marketplace-insights/resources/item_sales/methods/search#_samples
