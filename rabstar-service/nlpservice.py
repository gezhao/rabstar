import json
'''
import os.path
import sys
import webbrowser
import json
import os
import re
import urllib2
import mysql.connector



try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


##=============================================================================
## Constant Layer
##

CLIENT_ACCESS_TOKEN = '1982b51e247b49fe9020d2c2d1d78e9c'
DEV_ACCESS_TOKEN = '9a5df764d0a64db2a025483d51936008'

'''

##=============================================================================
## Query layer
##



##=============================================================================
## Util Layer
##


##=============================================================================
## Knowledge layer
##



	
##=============================================================================
## Service Layer
##




'''

## from NLP understanding, we know what is next to do
def getMsgFromNLPInsight(insightJsonObj):
	if(insightJsonObj is None):
		return "Not supported yet, say help to know the available commands"
	actionIncomplete = insightJsonObj['result'].get('actionIncomplete', False)
	if actionIncomplete:
		return insightJsonObj['result']['fulfillment']['speech']
	else:
		return actmsg()
  



def nlpinit():
	global inited
	global ai
	if(not inited):
		ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
		inited=True
'''		
def callnlp(msg, session):
	x= json.loads('{"name":"George"}')
	response = x
	return response
                	


