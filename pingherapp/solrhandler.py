import urllib2
import json

def solrcall(string):
	
	#Getting SOLR Hosted URL and docs
	inurl = "http://54.212.247.174:8983/solr/pingher_nort/select?q="+urllib2.quote(string)+"&wt=json"
	data = urllib2.urlopen(inurl)
	docs = json.load(data)['response']['docs']
	print string
	
	tweet = (docs[0]['tweet_text'])
	 
	return tweet