import sys
import requests
import urllib2
import itertools
from bs4 import BeautifulSoup
pageNumber = 1
max_number = 133
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
for number in range(pageNumber, max_number + pageNumber):
	url = opener.open("http://www.amazon.com/Apple-iPhone-16GB-Unlocked-Phone/product-reviews/B00NQGP42Y/ref=cm_cr_pr_btm_link_3?ie=UTF8&showViewpoints=1&sortBy=bySubmissionDateDescending&pageNumber="+str(number))
	soup = BeautifulSoup(url)
	# Review = soup.find('div', id='revMH').find('span','MHRHead').renderContents()
	# Title = soup.find('div', id='revMHRL').find('span','a-size-base a-text-bold').renderContents()
	# Author = soup.find('div', id='revMHRL').find('span','a-size-normal').find('a','noTextDecoration').renderContents()
	# Rating = soup.find('div', id='revMHRL').find('div','a-icon-row a-spacing-none').find('a')['title']
	Author = soup.findAll('div',id='cm_cr-review_list')
	# Author[0].find('a','noTextDecoration')
	print("")
	print("<------- Title : ------->")
	for a in Author:
	    names = a.findAll('a','a-size-base a-link-normal review-title a-color-base a-text-bold')
	    for name in names:
	    	print("")
	        print name.renderContents() 
	    # authors = a.findAll('a','a-size-base a-link-normal author')
	    # review = a.findAll('span','a-size-base review-text')
	    # date = a.findAll('span','a-size-base a-color-secondary review-date')
	    # rating = a.findAll('span','a-icon-alt')
	    # for name in names:	    		    	
	    #     print name.renderContents()		
     #    for name1 in authors:	    		    	
	    #     print name1.renderContents()
     #    for name2 in review:	    		    	
	    #     print name2.renderContents()
     #    for name3 in date:	    		    	
	    #     print name3.renderContents()
     #    for name4 in rating:	    		    	
	    #     print name4.renderContents()

	print("")
	print("<------- Author : ------->")
	for a in Author:
	    names = a.findAll('a','a-size-base a-link-normal author')
	    for name in names:
	    	print("")
	        print name.renderContents()        
	print("")
	print("<------- Review : ------->")
	for a in Author:
	    names = a.findAll('span','a-size-base review-text')
	    for name in names:
	    	print("")
	        print name.renderContents()
	print("")
	print("<------- Date : ------->")
	for a in Author:
	    names = a.findAll('span','a-size-base a-color-secondary review-date')
	    for name in names:
	    	print("")
	        print name.renderContents()        
	print("")
	print("<------- Rating : ------->")
	for a in Author:
	    names = a.findAll('span','a-icon-alt')
	    for name in names:
	    	print("")
	        print name.renderContents()        
	print("")





	# print("<------- Review Title : ------->")
	# for x in Author:
	#     title = x.findAll('a','a-size-base a-link-normal review-title a-color-base a-text-bold')
	#     for finaltitle in title:
	#     	print("")
	#         print finaltitle.renderContents()
	# print("")
	# print("<------- Review Content : ------->")
	# for y in Author:
	# 	review = y.findAll('span','MHRHead')
	# 	for content in review:
	# 		print("")
	# 		print content.renderContents()
	# print("")
	# print("<------- Review Rating : ------->")
	# for z in Author:
	# 	rating = z.findAll('a')['title']
	# 	for ratingfinal in rating:
	# 		print("")





	# print("")
	# print("**************************** $$$ *******************")
	# print("")
	# print ("Title : "+ Title)
	# print("")
	# print ("Author Name : "+Author)
	# print("")
	# print ("Review Content:  "+Review)
	# print("")
	# print ("Review Rating:  "+Rating)
	# print("")
