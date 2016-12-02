import urllib2
import json

def solrcall(string):
	
	#Getting SOLR Hosted URL and docs
	inurl = 'http://localhost:8983/solr/sampleshit/select?q=*:*&wt=json' 
	data = urllib2.urlopen(inurl)
	docs = json.load(data)['response']['docs']
	
	print string
	
	tweet = str(docs[1]['tweet_text']) 

	return tweet