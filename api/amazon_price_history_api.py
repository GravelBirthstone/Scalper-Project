import requests

url = "https://amazon-price-history.p.rapidapi.com/api/us/price_history"

querystring = {"asin":"B01LOP8EZC", "price_type":"amazon"}

headers = {
    'x-rapidapi-key': "38e058ddb8msh0ab4bb9902ac5b2p1d7aa3jsn10ae3807ccee",
    'x-rapidapi-host': "amazon-price-history.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
