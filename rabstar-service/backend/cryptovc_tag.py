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
type = "vc"
class CryptoVCClass:
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
		if(field=="score"):
			return self.score
		return "NA"

CRYPTO_EXCHANGE_CSV="./backend/CryptoList/Crypto VC's.csv"

def getCryptoVCList():
	return readFromCsv(CRYPTO_EXCHANGE_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')



def printVC(vc, items):
	c=vc
	"""
	print "--------------------------VC profile-------------------"
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
		vcList = []
		for row in reader:
			if(row[0]):
				vc = CryptoVCClass()
				vc.name=rr(row[0])
				vc.url=rr(row[1])
				vc.twitter=rr(row[2])
				vc.contactPage=rr(row[3])
				vc.email=rr(row[4])				
				vc.ceoName=rr(row[5])
				vc.ceoTwitter=rr(row[6])
				vc.ceoEmail=rr(row[7])
				#printVC(vc)
				vcList.append(vc)
		return vcList
		

## ---------------------------------------------------------------------------------------		
## Test

def query(qry):	
	t=util.getQuery(qry)
	items=[]
	
	if (t[0]==type):
		list= getCryptoVCList()
		cand=[]
		count=0
		for vc in list:
			field = vc.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the vc which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printVC(vc, items)
				cand.append(vc)			
		print "------------Total:", count
	return items
