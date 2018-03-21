##===========================================================================================================
# 					BlockChain ICO Tag Management  
#					Author: George Zhao
#					Created Date: 3/1/2018
# Summary: 
#
##===========================================================================================================

def getQuery(qry):
	items = qry.split(" ")
	ti = 0 #table index
	fi = 0 #field index
	ki = 0 #keyword index
	i=0
	for item in items:
		i=i+1
		if (item == "from"):
			ti=i
		if (item == "where"):
			fi=i
		if (item == "like"):
			ki=i
	str = items[ki]
	insides = str.split("%")
	t = (table,field,keyword) = (items[ti], items[fi], insides[1])
	return t


def getType(qry):
	if(qry=="hi" or qry=="example" or qry=="help"):
		return "help"
	items = qry.split(" ")
	ti = 0 #table index
	i=0
	for item in items:
		i=i+1
		if (item == "from"):
			ti=i
			return items[ti]
	return ""	


def outScore(index, path,  scoreDB):
	file = open (path, "w")
	for key in scoreDB:
		file.write(str(index)+","+key+","+str(scoreDB[key]+"\n"))
	file.close()