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
type="media"

class CryptoMediaClass:
	name = ""
	url = ""
	twitter = ""
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
			
		if(field=="score"):
			return self.score
		return "NA"

CRYPTO_MEDIA_CSV="./backend/CryptoList/Crypto Media.csv"

def getCryptoMediaList():
	return readFromCsv(CRYPTO_MEDIA_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')



def printMedia(media, items):
	c=media
	"""
	print "--------------------------Media profile-------------------"
	print "name=",c.name
	print "url=",c.url
	print "twitter=",c.twitter
	print 
	"""
	items.append((c.toJSON(), c.score))

## Implementation
## ---------------------------------------------------------------------------------------

def readFromCsv(filename):
	with open(filename, mode='r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		mediaList = []
		for row in reader:
			if(row[0]):
				media = CryptoMediaClass()
				media.name=rr(row[0])
				media.url=rr(row[1])
				media.twitter=rr(row[2])

				#printMedia(media)
				mediaList.append(media)
		return mediaList
		


# Return the list of medias based on qry
def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]==type):
		list= getCryptoMediaList()
		cand=[]
		count=0
		for media in list:
			field = media.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the exchange which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printMedia(media, items)
				cand.append(media)
			
		print "------------Total:", count
	return items
		

