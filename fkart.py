from bs4 import BeautifulSoup
import sys
import os
import urllib2
import itertools
import requests
import MySQLdb
import json
import simplejson as json

conn=MySQLdb.connect (host ="localhost",user="root",passwd="root",db="flipkart")    
product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
content = opener.open('http://www.flipkart.com/search?otracker=start&q='+product).read()
soup1 = BeautifulSoup(content)
link  = ["http://www.flipkart.com" + x.find('a')['href'] for x in soup1.find('div','old-grid').findAll('div','pu-title fk-font-13')]
# outfile = open("./flipkartmobiles.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerow(["Title","price","keyFeatures","specs"])
for data in link:
    #links = url.find('a')['href']
    #print ("http://www.flipkart.com"+links)
    # print (" ")
    #for data in links:      	
        raw = opener.open(data).read()
        soup = BeautifulSoup(raw)
        title = soup.findAll('h1','title')
        for eachitem in title:
                name1 = eachitem.text.strip().encode('utf-8')
                name1 = "'"+name1+"'"                            

        price = soup.findAll('span','selling-price omniture-field')
        for eachprice in price:
                price1 = eachprice.text.strip().encode('utf-8')
                price1 = "'"+price1+"'"                               
        keyfeat12 = {}
        keyfeatures = soup.findAll('div','keyFeatures specSection')        
        for keys in keyfeatures:
        	keyfeat = keys.text.strip().encode('utf-8')
        	keyfeat12 = "'"+keyfeat+"'"				

        main_dict = {}
        soup = BeautifulSoup(requests.get(data).text)
        Specification = soup.findAll('table','specTable')        
        #Specification.findAll('tr',recursive=False)
        [main_dict.update(x) for x in [dict([tuple([y.renderContents().strip() for y in x.findAll('td')]) for x in Spec.findAll('tr') if len(x.findAll('td'))==2]) for Spec in Specification]]                
        cursore=conn.cursor()       
        datum="insert into fkartmobile (name,price,keyfeatures,specs,url) values (%s , %s , %s , %s, %s)"                                                        
        cursore.execute(datum,(name1,price1,json.dumps(keyfeat12),json.dumps(main_dict),data))
        conn.commit()                


                # print key = data.findAll('td')[0]
                # value = data.findAll('td')[1]
                # print d[key] = d[value]                    
        # print(" ")
        # results.append(d)      
        # print d
        

    
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
