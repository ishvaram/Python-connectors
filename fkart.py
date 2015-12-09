from bs4 import BeautifulSoup
import csv
import sys
import urllib2
import itertools
import requests

product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
content = opener.open('http://www.flipkart.com/search?otracker=start&q='+product).read()
soup1 = BeautifulSoup(content)
link  = ["http://www.flipkart.com" + x.find('a')['href'] for x in soup1.find('div','old-grid').findAll('div','pu-title fk-font-13')]
outfile = open("./flipkartmobiles.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Title","price","keyFeatures","specs"])
results = [] 
for data in link:
    #links = url.find('a')['href']
    #print ("http://www.flipkart.com"+links)
    # print (" ")
    #for data in links: 
        print data
        d = {}      
        raw = opener.open(data).read()
        soup = BeautifulSoup(raw)
        title = soup.findAll('h1','title')
        for eachitem in title:
                print("Item name : "+ eachitem.renderContents())
        print(" ")        
        price = soup.findAll('span','selling-price omniture-field')
        for eachprice in price:
                print("Item Price : "+ eachprice.renderContents())
        print(" ") 
        Specification = soup.findAll('table','specTable')
        for data in Specification:
                print data.text
                # print key = data.findAll('td')[0]
                # value = data.findAll('td')[1]
                # print d[key] = d[value]
        print(" ")        
        keyFeatures = soup.findAll('div',class_='keyFeatures specSection')
        for keys in keyFeatures:
                print keys.text
        # print(" ")
        # results.append(d)      
        # print d
        
writer.writerows([title,price,keyFeatures,Specification])
    
# for keys in Specification:
#         for key in keys:
#                 for data in key:
#                         print data

# print(" ")        
# keyFeatures = soup.findAll('div',class_='keyFeatures specSection')
# for keys in keyFeatures:
#         print keys.getText()
# print(" ")         

# print('Product title : '+ str(title))

# print ('Product Price : ' + str(price))
# print(" ")
# print ('Product Specs : ' + str(Specification))
# print(" ")
# print ('Product keyFeatures : ' + str(keyFeatures))
