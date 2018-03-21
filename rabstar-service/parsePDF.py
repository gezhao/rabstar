##===========================================================================================================
# 					Rabstar Blockchain PDF Parser  
#					Author: George Zhao
#					Created Date: 3/18/2018
#
##===========================================================================================================


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


filename = './data/bitcoin.pdf' 

debug=0

def convert(fname, pages=None):
	if not pages:
		pagenums = set()
	else:
		pagenums = set(pages)

	output = StringIO()
	manager = PDFResourceManager()
	converter = TextConverter(manager, output, laparams=LAParams())
	interpreter = PDFPageInterpreter(manager, converter)

	infile = file(fname, 'rb')
	for page in PDFPage.get_pages(infile, pagenums):
		interpreter.process_page(page)
	infile.close()
	converter.close()
	text = output.getvalue()
	output.close
	return text 
    


def wordsInMap(words):
	map={}
	for word in words:
		if(word in map):
			map[word]=map[word]+1
		else:
			map[word]=1
	return map

def getWordsFromText(text):
	tokens = word_tokenize(text.decode("utf-8"))
	dbg(tokens)
	#we'll create a new list which contains punctuation we wish to clean
	punctuations = ['(',')',';',':','[',']',',']
	#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
	stop_words = stopwords.words('english')
	#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
	keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]
	return keywords
	
	

## Utility
## ---------------------------------------------------------------------------------------

def dbg(item):
	if(debug!=0):
		print item


def main():
	#text = readTextFromPDF(filename)
	text =convert(filename)
	words = getWordsFromText(text)
	map=wordsInMap(words)
	
	for key in map:
		print map[key],key.encode("utf-8")

if __name__ == "__main__":
	main()
