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
type="writer"

class CryptoWriterClass:
	name = ""
	publication = ""
	url = ""
	twitter = ""
	email = ""
	article = ""
	#UI- score for this entity
	score = 10
	
	#UI- JSON object from the object
	def toJSON(self):
        	return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            
		
	def getByField(self, field):
		if(field=="name"):
			return self.name
		if(field=="publication"):
			return self.publication
		if(field=="twitter"):
			return self.twitter
		if(field=="url"):
			return self.url
		if(field=="email"):
			return self.email
		if(field=="article"):
			return self.article

		if(field=="score"):
			return self.score
		return "NA"

CRYPTO_WRITER_CSV="./backend/CryptoList/Crypto Journalists.csv"

def getCryptoWriterList():
	return readFromCsv(CRYPTO_WRITER_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')


def printWriter(writer, items):
	c=writer
	"""
	print "--------------------------Writer profile-------------------"
	print "name=",c.name
	print "url=",c.url
	print "twitter=",c.twitter
	print "publication=",c.publication
	print "email=",c.email 
	print "article=",c.article
	print 
	"""
	items.append((c.toJSON(), c.score))

## Implementation
## ---------------------------------------------------------------------------------------

def readFromCsv(filename):
	with open(filename, mode='r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		writerList = []
		for row in reader:
			if(row[0]):
				writer = CryptoWriterClass()
				writer.name=rr(row[0])
				writer.publication=rr(row[1])
				writer.url=rr(row[2])
				writer.twitter=rr(row[3])
				writer.email=rr(row[4])
				writer.article=rr(row[5])

				#printWriter(writer)
				writerList.append(writer)
		return writerList
		


# Return the list of writers based on qry
def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]==type):
		list= getCryptoWriterList()
		cand=[]
		count=0
		for writer in list:
			field = writer.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the exchange which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printWriter(writer, items)
				cand.append(writer)
			
		print "------------Total:", count
	return items
		

