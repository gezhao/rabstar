##===========================================================================================================
# 					BlockChain ICO Tag Management  
#					Author: George Zhao
#					Created Date: 3/1/2018
# Summary: 
#
##===========================================================================================================
import csv
import sys
import util
import json

## Service
## ---------------------------------------------------------------------------------------
debug = 0

class CryptoICOClass:
	name = ""
	url = ""
	twitter = ""
	email = ""
	contactPage = ""
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
		if(field=="score"):
			return self.score
		return "NA"

CRYPTO_ICO_CSV="./backend/CryptoList/Crypto ICO's.csv"

def getCryptoICOList():
	return readFromCsv(CRYPTO_ICO_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')



def printObject(ico, items):
	c=ico
	"""
	print "--------------------------Company profile-------------------"
	print "name=",c.name
	print "url=",c.url
	print "twitter=",c.twitter
	print "contactPage=",c.contactPage
	print "email=",c.email 
	print "ceoName=",c.ceoName
	print "ceoTwitter=",c.ceoTwitter
	print "ceoEmil=",c.ceoEmail
	print 
	"""
	items.append((c.toJSON(), c.score))

## Implementation
## ---------------------------------------------------------------------------------------

def readFromCsv(filename):
	with open(filename, mode='r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		icoList = []
		for row in reader:
			if(row[0]):
				ico = CryptoICOClass()
				ico.name=rr(row[0])
				ico.url=rr(row[1])
				ico.twitter=rr(row[2])
				ico.contactPage=rr(row[3])
				ico.email=rr(row[4])
				ico.ceoName=rr(row[5])
				ico.ceoTwitter=rr(row[6])
				ico.email=rr(row[7])

				icoList.append(ico)
		return icoList
		

# Example Queries
#     select * from ico where name like %Aerium%

# Return the list of objects based on qry
def query(qry):
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]=="ico"):
		list= getCryptoICOList()
		cand=[]
		count=0
		for ico in list:
			field = ico.getByField(t[1])
			dbg(field+":"+t[2])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the company which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printObject(ico, items)
				cand.append(ico)
		print "------------Total:", count
	return items	
		
