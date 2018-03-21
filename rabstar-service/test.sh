	#print "--------------------------Event profile-------------------"
	#print "name="
	#print "url="
	#print "twitter="
	#print "contactPage="
	#print "email="
	#print "eventDate="
	#print "city="
	#print "country="

	#print "--------------------------Writer profile-------------------"
	#print "name="
	#print "url="
	#print "twitter="
	#print "publication="
	#print "email="
	#print "article="
	#print 

	#print "--------------------------Fbgroup profile-------------------"
	#print "url="
	#print "followers="
	#print 

	#print "--------------------------Redditgroup profile-------------------"
	#print "url="
	#print "followers="
	print

	#print "--------------------------Company profile-------------------"
	#print "name="
	#print "url="
	#print "twitter="
	#print "contactPage="
	#print "email="
	#print "ceoName="
	#print "ceoTwitter="
	#print "ceoEmil="
	#print 

	#print "--------------------------Media profile-------------------"
	#print "name="
	#print "url="
	#print "twitter="
	#print 




	#print "--------------------------VC profile-------------------"
	#print "name="
	#print "url="
	#print "twitter="
	#print "contactPage="
	#print "email="
	#print "ceoName="
	#print "ceoTwitter="
	#print "ceoEmil="


	#print "--------------------------Exchange profile-------------------"
	#print "name="
	#print "url="
	#print "twitter="
	#print "contactPage="
	#print "email="
	#print "ceoName="
	#print "ceoTwitter="
	#print "ceoEmil="
	#print "blog="
python engine.py "select * from event where city like %San Francisco%"
python engine.py "select * from writer where name like %Jeff%"
python engine.py "select * from fbgroup where url like %eth%"
python engine.py "select * from redditgroup where url like %bitcoin%"
python engine.py "select * from startup where ceoName like %matthew%"
python engine.py "select * from media where name like %bitcoin%"
python engine.py "select * from vc where name like %goldman%"
python engine.py "select * from exchange where name like %bitstamp%"

