import requests

ps3_url = "https://api.bestbuy.com/v1/products/6820583.json?show=sku,name,salePrice&apiKey=4GDY4KJaNUeKbtoP9uTbTBXT"
ps4_url = "https://api.bestbuy.com/v1/products/5850905.json?show=sku,name,salePrice&apiKey=4GDY4KJaNUeKbtoP9uTbTBXT"
ps5_url = "https://api.bestbuy.com/v1/products/6426149.json?show=sku,name,salePrice&apiKey=4GDY4KJaNUeKbtoP9uTbTBXT"

ps3 = requests.request("GET", ps3_url)
ps4 = requests.request("GET", ps4_url)
ps5 = requests.request("GET", ps5_url) 

print(ps3.text)
print(ps4.text)
print(ps5.text)
