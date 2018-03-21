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
debug = 4
type = "event"
class CryptoEventClass:
	name = ""
	url = ""
	eventDate = ""
	city = ""
	country = ""
	twitter = ""
	contactpage = ""
	email = ""
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
		if(field=="eventDate"):
			return self.eventDate
		if(field=="city"):
			return self.city
		if(field=="country"):
			return self.country
		if(field=="twitter"):
			return self.twitter
		if(field=="contactpage"):
			return self.contactpage
		if(field=="email"):
			return self.email
		if(field=="score"):
			return self.score
		return "NA"

#UI- Directory needs to be the web app location
CRYPTO_EVENT_CSV="./backend/CryptoList/Crypto Events.csv"

def getCryptoEventList():
	return readFromCsv(CRYPTO_EVENT_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item

#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')
		


def printEvent(event, items):
	c=event
	"""
	print "--------------------------Event profile-------------------"
	print "name=",c.name
	print "url=",c.url
	print "twitter=",c.twitter
	print "contactPage=",c.contactPage
	print "email=",c.email 
	print "eventDate=",c.eventDate
	print "city=",c.city
	print "country=",c.country
	print 
	"""
	#UI- Each item has a score
	items.append((event.toJSON(), event.score))
	#items.append(vars(event))

## Implementation
## ---------------------------------------------------------------------------------------

def readFromCsv(filename):
	with open(filename, mode='r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		eventList = []
		for row in reader:
			if(row[0]):
				event = CryptoEventClass()
				event.name=rr(row[0])
				event.url=rr(row[1])
				event.eventDate=rr(row[2])
				event.city=rr(row[3])
				event.country=rr(row[4])
				event.twitter=rr(row[5])
				event.contactPage=rr(row[6])
				event.email=rr(row[7])
				#printEvent(event)
				eventList.append(event)
		return eventList
		

## ---------------------------------------------------------------------------------------		
## Test

		
	
		
def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]==type):
		list= getCryptoEventList()
		cand=[]
		count=0
		for event in list:
			field = event.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the exchange which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printEvent(event,items)
				cand.append(event)
			
		print "------------Total:", count
	return items