import csv
from bs4 import BeautifulSoup
import sys
import os
import urllib2
import itertools 
from itertools import takewhile
import requests
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import simplejson as json   
product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
content = opener.open('http://www.flipkart.com/search?otracker=start&q='+product).read()
soup1 = BeautifulSoup(content)
link  = ["http://www.flipkart.com" + x.find('a')['href'] for x in soup1.find('div','old-grid').findAll('div','pu-title fk-font-13')]
# f = open("testataflip.csv", 'wt')
# writer = csv.writer(f)
# writer.writerow(('Product Name', 'Price', 'keyFeatures','Specification','URL'))
json_key = json.load(open('mypy-4c1d85515f48.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
# We can open the sheet by below options
wks = gc.open_by_key("replace_your_sheet_id").sheet1
#wks = gc.open("replace_your_sheet_name").sheet1
#wks = gc.open_by_URL("replace_your_url_here").sheet1

count = 0
for data in link:       
        raw = opener.open(data).read()
        soup = BeautifulSoup(raw)
        image = soup.find('div','imgWrapper').find('img')['data-src']
        title = soup.findAll('h1','title')
        for eachitem in title:
                name1 = eachitem.text.strip().encode('utf-8')

                #name1 = "'"+name1+"'"                            

        price = soup.findAll('span','selling-price omniture-field')
        for eachprice in price:
                price1 = eachprice.text.strip().encode('utf-8')
                #price1 = "'"+price1+"'"                               
        keyfeat12 = {}
        keyfeatures = soup.find('div',{'id':'veiwMoreSpecifications'}).findAll('ul',{'class':'keyFeaturesList'})        
        for keys in keyfeatures:
            keyfeat = keys.text.strip().encode('utf-8')
            keyfeat12 = keyfeat             

        main_dict = {}
        soup = BeautifulSoup(requests.get(data).text)
        Specification = soup.findAll('table','specTable')        
        #Specification.findAll('tr',recursive=False)
        [main_dict.update(x) for x in [dict([tuple([y.renderContents().strip() for y in x.findAll('td')]) for x in Spec.findAll('tr') if len(x.findAll('td'))==2]) for Spec in Specification]]                
        #datum = {"Name" : "'"+name1+"'", "Price" : "'"+price1+"'","Keyfeatures":"'"+json.dumps(keyfeat12)+"'","Specs":"'"+json.dumps(main_dict)+"'","URL":"'"+data+"'"}
        datum = {name1 ,price1,json.dumps(keyfeat12),json.dumps(main_dict),data}
        count += 1
        print "data for url " + str(count)
        featu = json.dumps(keyfeat12,ensure_ascii = False)
        dicto = json.dumps(main_dict,ensure_ascii = False)
        wks.append_row([name1,image,price1,featu,dicto,data]) 
        #writer.writerow((name1,price1,json.dumps(keyfeat12),json.dumps(main_dict),data))
        #writer.writerows(datum)