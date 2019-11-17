import requests
import webbrowser
import re
import botocore
import boto3

from bs4 import BeautifulSoup
from time import sleep

retailers = {
    "ikea.c",
    "apple.c",
    "walmart.c",
    "target.c",
    "bestbuy.c",
    "chapters.c",
    "wayfair.c",
    "homedepot.c",
    "rona.c",
    "hayneedle.c",
    "furniture.c",
    "overstock.c",
    "ashleyhomestore.c",
    "article.c"
}

# takes in a path to an image and returns the first product result from that image
def reverse_image_search(image_path):
    # add User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }

    searchUrl = "http://www.google.com/searchbyimage/upload"
    multipart = {
        "encoded_image": (image_path, open(image_path, "rb")),
        "image_content": "",
    }
    # do the image search with a POST request
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    url = response.headers["Location"]

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")
    links = soup.findAll("a")

    first_product_link = ""
    link_found = False

    for link in links:
        if link_found == True:
            break
        # check that link is not null
        if link.get("href") is not None:
            # check if the link is a valid retailer link
            for website in retailers:
                if website in link.get("href") and link.get("href").startswith("http"):
                    first_product_link = link.get("href")
                    link_found = True
                    break

    return first_product_link

