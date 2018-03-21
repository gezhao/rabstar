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
debug = 0

class CryptoCompanyClass:
	name = ""
	url = ""
	twitter = ""
	contactPage = ""
	email = ""
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

CRYPTO_COMPANY_CSV="./backend/CryptoList/Crypto Companies.csv"

def getCryptoCompanyList():
	return readFromCsv(CRYPTO_COMPANY_CSV)

## Utility
## ---------------------------------------------------------------------------------------


def dbg(item):
	if(debug!=0):
		print item
	
#UI - When read from .csv, need to decode	
def rr(field):
	return field.decode('utf-8')



def printCompany(company, items):
	c=company
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
		companyList = []
		for row in reader:
			if(row[0]):
				company = CryptoCompanyClass()
				company.name=rr(row[0])
				company.url=rr(row[1])
				company.twitter=rr(row[2])
				company.contactPage=rr(row[3])
				company.email=rr(row[4])
				company.ceoName=rr(row[5])
				company.ceoTwitter=rr(row[6])
				company.email=rr(row[7])
				#printCompany(company)
				companyList.append(company)
		return companyList
		


# Example Queries
#     select * from startup where name like %Aerium%

# Return the list of companies based on qry
def query(qry):	
	t=util.getQuery(qry)
	dbg(t)
	items=[]
	
	if (t[0]=="startup"):
		list= getCryptoCompanyList()
		cand=[]
		count=0
		for company in list:
			field = company.getByField(t[1])
			if (field=="NA"):
				continue
			index= field.lower().find(t[2].lower())
			
			#Find the company which matches the field
			if index<0:
				continue
			else:
				count=count+1
				printCompany(company, items)
				cand.append(company)
			
		print "------------Total:", count
	return items
		

