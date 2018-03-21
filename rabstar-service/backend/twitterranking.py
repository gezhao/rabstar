##===========================================================================================================
# 					Rabstar ICO Ranking System  
#					Author: George Zhao
#					Created Date: 3/1/2018
#
##===========================================================================================================


import webbrowser
import util

## Service
## ---------------------------------------------------------------------------------------

TWITTER_FILE = "CryptoList/twitters.txt"
TWITTER_RANKING = "CryptoList/out_score_twitter"
#startIndex is the left over for the new ranking to start with
def twitterRanking(startIndex):
	file = open(TWITTER_FILE,'r')
	lines = file.readlines()
	scoreDB={} # A map object for all ranking
	k=0
	for line in lines:
		k=k+1
		if(k<startIndex):
			continue
		print "step of K:",k,line
		score = ranking(line.strip(), scoreDB)
		if(score>10):
			util.outScore(k, TWITTER_RANKING+str(startIndex)+".txt", scoreDB)
		



## Utility
## ---------------------------------------------------------------------------------------

def openCheck(url):
	new = 1
	webbrowser.open(url,new=new)





## Implementation
## ---------------------------------------------------------------------------------------

# The ranking process for check the url and give a score and save the score
# Ranking 0: ignore 1:Interesting 2:Good 3:Outstanding 4:Top score
#
def ranking(url, scoreDB):
	openCheck(url)
	ranking = raw_input()
	scoreDB[url] = ranking
	return ranking
	