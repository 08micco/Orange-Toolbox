import requests
import bs4
import json

base_url = "https://www.asphaltgold.com/"

session = requests.Session()


def get_stock():
    r = requests.get(url=base_url + "/products.json")
    print(r.text)


get_stock()
