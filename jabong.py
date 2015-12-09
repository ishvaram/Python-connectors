import sys
import requests
import urllib2
import itertools
from bs4 import BeautifulSoup
import re

count = 0
for index in range(1,12):
    # url = "http://www.jabong.com/shoes/Adidas--adidas-originals--Nike--Puma--Red_Chief--Red_Tape--top-shop--Van_Heusen--vans--Woodland/?tt=shoes&rank=1&qc=shoes&page=1&limit=200"
    url = "http://www.jabong.com/find/sony/?q=sons&tt=&rank=0&qc=sony"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    g_data = soup.find_all("section",{"class":"row search-product animate-products"})[0]    
    total_products = int(soup.find_all("p",{"class":"filter-prod-count"})[0].text.replace("PRODUCTS",""))
    
    for items in g_data:
        try:
            img_url = items.contents[0].find_all("img")[0].get("src")
        except:
            pass
        try:
            name = items.contents[0].find_all("div",{"class":"h4"})[0].text
        except:
            pass
        try:
            price = items.contents[0].find_all("span",{"class":"standard-price"})[0].text
        except:
            pass
        try:
            sizes = items.contents[0].find_all("div",{"class":"avail-size"})[0]
            avail_sizes =[]
            for s in sizes:
                if(s.text!="Sizes"):
                    avail_sizes.append(int(s.text))
        except:
            pass
        
        print("Image_url = " +img_url)
        print("Product Name : " +name)
        print("Price(INR) : " +price)
        print("Available Sizes : " +str(avail_sizes))
        print("\n")
        count=count+1;

        if(count==total_products):
            break;

        
    

    
