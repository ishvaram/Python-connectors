from bs4 import BeautifulSoup
import sys
import urllib2
import itertools
import requests
import MySQLdb

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
                name1 = eachitem.text
                name1 = "'"+name1+"'"                            

        price = soup.findAll('span','selling-price omniture-field')
        for eachprice in price:
                price1 = eachprice.text 
                price1 = "'"+price1+"'"                               

        keyFeatures = soup.findAll('div',class_='keyFeatures specSection')
        for keys in keyFeatures:
                keyFeatures1 = keys.text
                keyFeatures1 = "'"+keyFeatures1+"'"

        Specification = soup.findAll('table','specTable')
        for data in Specification:
                specs1 = data.text
                specs1 = "'"+specs1+"'"

        cursore=conn.cursor()       
        x="insert into fkartmobile (name,price,keyfeatures,specs) values (%s , %s , %s , %s)"%(name1,price1,keyFeatures1,specs1)        
        cursore.execute(x)
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
