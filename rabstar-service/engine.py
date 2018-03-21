"""A simple search engine in python."""
import sys
sys.path.insert(0, './backend')
import rabstar as rb

#See: https://github.com/jorendorff/tinysearch/blob/master/web.py


class Index:

    def search(self, query):
        return rb.run_query(query)

def main():

	if(len(sys.argv)<2):
		print "---------------------------------------------------------"
		print "filed:..."
		print "query: select * from <type> where <field> like %xxxx%"
		print 
		print "usage: engine.py <query>)"
		print "---------------------------------------------------------"
		return
	

	items=rb.run_query(sys.argv[1])
	print "testing...", items


if __name__ == "__main__":
	main()