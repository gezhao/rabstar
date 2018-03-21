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
type="redditgroup"

class CryptoRedditgroupClass:
	url = ""
	followers = ""
	#UI- score for this entity
	score = 10
	
	#UI- JSON object from the object
	def toJSON(self):
        	return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            
		
	def getByField(self, field):
		if(field=="url"):
			return self.url
		if(field=="followers"):
			return self.followers

		if(field=="score"):
			return self.score
		return "NA"

CRYPTO_REDDITGROUP_CSV="./backend/CryptoList/Reddit Crypto Groups.csv"

def getCryptoRedditgroupList():
	return readFromCsv(CRYPTO_REDDITGROUP_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')



def printRedditgroup(redditgroup, items):
	c=redditgroup
	"""
	print "--------------------------Redditgroup profile-------------------"
	print "url=",c.url
	print "followers=",c.followers
	print 
	"""
	items.append((c.toJSON(), c.score))

## Implementation
## ---------------------------------------------------------------------------------------

def readFromCsv(filename):
	with open(filename, mode='r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		redditgroupList = []
		for row in reader:
			if(row[0]):
				redditgroup = CryptoRedditgroupClass()
				redditgroup.url=rr(row[0])
				redditgroup.followers=rr(row[1])


				#printRedditgroup(redditgroup)
				redditgroupList.append(redditgroup)
		return redditgroupList
		


# Return the list of redditgroups based on qry
def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]==type):
		list= getCryptoRedditgroupList()
		cand=[]
		count=0
		for redditgroup in list:
			field = redditgroup.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the exchange which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printRedditgroup(redditgroup,items)
				cand.append(redditgroup)
			
		print "------------Total:", count
	
	return items	

