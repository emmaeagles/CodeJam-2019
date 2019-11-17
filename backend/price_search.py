import requests
import webbrowser
import re
import botocore
import boto3

from bs4 import BeautifulSoup
from time import sleep

def price_search(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }
# 
    # do the image search with a POST request
    response = requests.post(link, allow_redirects=False)
    # url = response.headers["Location"]
# 
    specific_page = requests.get(link, headers=headers)
    specific_soup = BeautifulSoup(specific_page.content, "lxml")
    print(specific_soup)

    prices = specific_soup.body.findAll(text=re.compile("^\$.*"))
    for price in prices:
        return price
    prices = specific_soup.body.findAll(text=re.compile(".*\$.*"))
    for price in prices:
        return price

    return None