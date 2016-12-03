import solrhandler
from wit import Wit
import json

def converse(Query):
	access_token = "HUYFSZATE2FRGLETGVWWTCHNSVTXBKDC" 


	def send(request, response):
	    print(response['text'])
	actions = {
	    'send': send,    
	}

	client = Wit(access_token=access_token, actions=actions)
	#Query=""
	data=client.converse(1,Query)
	X=""
	tweet=""
	for key in data['entities'].keys():
	   	X=X+" "+(data['entities'][key][0]['value'])
	mydict=json.load(open("mydict.json"))
	solr=True
	for key_list in mydict.keys():
		flag=True
		for key in data['entities'].keys():
			if str(data['entities'][key][0]['value']).upper() not in str(key_list):
				flag=False
		if flag:
			tweet=mydict[key_list]
			solr=False

	if solr:
		tweet=solrhandler.solrcall(X)
	
	return tweet

