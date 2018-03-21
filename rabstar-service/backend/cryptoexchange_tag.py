##===========================================================================================================
# 					Rabstar Blockchain Tag Management  
#					Author: George Zhao
#					Created Date: 3/1/2018
#
##===========================================================================================================
import csv
import sys
import util
import json

## Service
## ---------------------------------------------------------------------------------------
debug = 1
type = "exchange"
class CryptoExchangeClass:
	name = ""
	url = ""
	twitter = ""
	email = ""
	contactPage = ""
	blog = ""
	ceoName = ""
	ceoTwitter = ""
	ceoEmail = ""
	#UI- score for this entity
	score = 10
	
	#UI- JSON object from the object
	def toJSON(self):
        	return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            

	
	def getByField(self, field):
		if(field=="name"):
			return self.name
		if(field=="url"):
			return self.url
		if(field=="twitter"):
			return self.twitter
		if(field=="contactPage"):
			return self.contactPage
		if(field=="email"):
			return self.email
		if(field=="ceoName"):
			return self.ceoName
		if(field=="ceoTwitter"):
			return self.ceoTwitter
		if(field=="ceoEmail"):
			return self.ceoEmail
		if(field=="blog"):
			return self.blog
		if(field=="score"):
			return self.score
		return "NA"

CRYPTO_EXCHANGE_CSV="./backend/CryptoList/Crypto Exchanges.csv"

def getCryptoExchangeList():
	return readFromCsv(CRYPTO_EXCHANGE_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')


def printExchange(exchange, items):
	c=exchange
	"""
	print "--------------------------Exchange profile-------------------"
	print "name=",c.name
	print "url=",c.url
	print "twitter=",c.twitter
	print "contactPage=",c.contactPage
	print "email=",c.email 
	print "ceoName=",c.ceoName
	print "ceoTwitter=",c.ceoTwitter
	print "ceoEmil=",c.ceoEmail
	print "blog=",c.blog

	print 
	"""
	items.append((exchange.toJSON(), exchange.score))

## Implementation
## ---------------------------------------------------------------------------------------

def readFromCsv(filename):
	with open(filename, mode='r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		exchangeList = []
		for row in reader:
			if(row[0]):
				exchange = CryptoExchangeClass()
				exchange.name=rr(row[0])
				exchange.url=rr(row[1])
				exchange.twitter=rr(row[2])
				exchange.email=rr(row[3])
				exchange.contactPage=rr(row[4])
				exchange.blog=rr(row[5])
				exchange.ceoname=rr(row[6])
				exchange.ceoTwitter=rr(row[7])
				exchange.email=rr(row[8])
				#printExchange(exchange)
				exchangeList.append(exchange)
		return exchangeList
		

## ---------------------------------------------------------------------------------------		
## Test

def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]==type):
		list= getCryptoExchangeList()
		cand=[]
		count=0
		for exchange in list:
			field = exchange.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the exchange which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printExchange(exchange,items)
				cand.append(exchange)
			
		print "------------Total:", count
	return items