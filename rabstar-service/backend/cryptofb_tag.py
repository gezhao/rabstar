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
type="fbgroup"

class CryptoFbgroupClass:
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
CRYPTO_FBGROUP_CSV="./backend/CryptoList/Crypto Facebook Groups.csv"

def getCryptoFbgroupList():
	return readFromCsv(CRYPTO_FBGROUP_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')



def printFbgroup(fbgroup, items):
	c=fbgroup
	"""
	print "--------------------------Fbgroup profile-------------------"
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
		fbgroupList = []
		for row in reader:
			if(row[0]):
				fbgroup = CryptoFbgroupClass()
				fbgroup.url=rr(row[0])
				fbgroup.followers=rr(row[1])


				#printFbgroup(fbgroup)
				fbgroupList.append(fbgroup)
		return fbgroupList
		


# Return the list of fbgroups based on qry
def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]==type):
		list= getCryptoFbgroupList()
		cand=[]
		count=0
		for fbgroup in list:
			field = fbgroup.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the exchange which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printFbgroup(fbgroup, items)
				cand.append(fbgroup)
			
		print "------------Total:", count
	return items
		

