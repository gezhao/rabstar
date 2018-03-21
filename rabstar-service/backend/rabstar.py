##===========================================================================================================
# 					BlockChain Projects Search Engine  
#					Author: George Zhao
#					Created Date: 3/1/2018
# Summary: 
#	
#
##===========================================================================================================
import csv
import sys

import cryptostartup_tag
import cryptoico_tag
import cryptoexchange_tag
import cryptowriter_tag
import cryptoevent_tag
import cryptofb_tag
import cryptoredditgroup_tag
import cryptomedia_tag
import cryptovc_tag
import util
import twitterranking


## Service
## ---------------------------------------------------------------------------------------
def run_query(qry):
	items=[]
	type=util.getType(qry)
	if(type=="help"):
		items.append(("example 1==>  select * from event where city like %San Francisco%",1))
		items.append(("example 2==>  select * from writer where name like %jeff%",2))
		items.append(("example ...==>  select * from [table] where [column] like %xxx%",3))
		items.append(("need help==>  type 'help'",4))
		items.append(("-----------------------Table and Columns----------------",0))
		items.append(("-[event]- name,url,twitter,contactPage,email,eventDate,city,country",0))
		items.append(("-[writer]- name,url,twitter,publication,email,article",0))
		items.append(("-[redditgroup]- url,followers",0))
		items.append(("-[startup]- name,url,twitter,contactPage,email,ceoName,ceoTwitter,ceoEmil",0))
		items.append(("-[ico]- name,url,twitter,contactPage,email,ceoName,ceoTwitter,ceoEmil",0))
		items.append(("-[media]- name,url,twitter",0))
		items.append(("-[vc]- name,url,twitter,contactPage,email,ceoName,ceoTwitter,ceoEmil",0))
		items.append(("-[exchange]- name,url,twitter,contactPage,email,ceoName,ceoTwitter,ceoEmil,blog",0))		
		items.append(("-[fbgroup]- url,followers",0))
		return items

	if(type=="startup"):
		items=cryptostartup_tag.query(qry)
	if(type=="ico"):
		items=cryptoico_tag.query(qry)
	if(type=="exchange"):
		items=cryptoexchange_tag.query(qry)	
	if(type=="writer"):
		items=cryptowriter_tag.query(qry)
	if(type=="event"):
		items=cryptoevent_tag.query(qry)	
	if(type=="fbgroup"):
		items=cryptofb_tag.query(qry)
	if(type=="redditgroup"):
		items=cryptoredditgroup_tag.query(qry)
	if(type=="media"):
		items=cryptomedia_tag.query(qry)
	if(type=="vc"):
		items=cryptovc_tag.query(qry)
	return items


			
def printDBchema():
	print "--------------------------Event profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print "contactPage="
	print "email="
	print "eventDate="
	print "city="
	print "country="

	print "--------------------------Writer profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print "publication="
	print "email="
	print "article="
	print 

	print "--------------------------Fbgroup profile-------------------"
	print "url="
	print "followers="
	print 

	print "--------------------------Redditgroup profile-------------------"
	print "url="
	print "followers="
	print

	print "--------------------------Company profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print "contactPage="
	print "email="
	print "ceoName="
	print "ceoTwitter="
	print "ceoEmil="
	print 

	print "--------------------------Media profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print 


	print "--------------------------Company profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print "contactPage="
	print "email="
	print "ceoName="
	print "ceoTwitter="
	print "ceoEmil="
	print 


	print "--------------------------VC profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print "contactPage="
	print "email="
	print "ceoName="
	print "ceoTwitter="
	print "ceoEmil="


	print "--------------------------Exchange profile-------------------"
	print "name="
	print "url="
	print "twitter="
	print "contactPage="
	print "email="
	print "ceoName="
	print "ceoTwitter="
	print "ceoEmil="
	print "blog="


## ---------------------------------------------------------------------------------------		
def main():
	global debug
	debug = 0
	if(len(sys.argv)<2):
		print "---------------------------------------------------------"
		print "filed:..."
		print "query: select * from <type> where <field> like %xxxx%"
		print 
		print "usage: rabstar.py <query>)"
		print "---------------------------------------------------------"
		return
	
	para1 = sys.argv[1]
	items=[]
	if(para1.find("ranking") >=0):
		index = int(sys.argv[2])
		twitterranking.twitterRanking(index)
	elif(para1.find("schema") >=0):
		printDBchema()
	else:
		items=run_query(sys.argv[1])
	print "testing...", items


if __name__ == "__main__":
	main()
