import urllib2
import json

def solrcall(string):
	
	#Getting SOLR Hosted URL and docs
	inurl = "http://54.191.145.231:8984/solr/IRF16P1/select?q="+string+"&wt=json" 
	data = urllib2.urlopen(inurl)
	docs = json.load(data)['response']['docs']
	
	print string
	
	tweet = str(docs[1]['tweet_text']) 
	#tweet="Donald Trump"
	return tweet