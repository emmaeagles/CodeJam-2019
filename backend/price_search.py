import requests
import webbrowser
import re
import botocore
import boto3

from bs4 import BeautifulSoup
from time import sleep

# attempt to find a price on the given URL
def price_search(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }

    try:
        specific_page = requests.get(link, headers=headers, timeout=10)
        specific_soup = BeautifulSoup(specific_page.content, "lxml")

        price = specific_soup.body.find(text=re.compile(r"^\$.*"))
        if price is not None and price != "":
            return price
    except Exception as ex:
        print(ex)

    return None
