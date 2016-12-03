import urllib2
import json

def solrcall(string):
	
	#Getting SOLR Hosted URL and docs
	screen_name=""
	tweet=""
	if "tweets from" in string.lower():
		screen_name=string.lower().replace("tweets from ","")
		screen_name=screen_name.lower().replace(" ","")
		inurl="http://54.212.247.174:8983/solr/pingher/select?q=screen_name:"+urllib2.quote(screen_name)+"&wt=json"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		size=5
		if len(docs)<5:
			size=len(docs)
		for i in range(size):
			tweet+=(docs[i]['tweet_text'][0])
			tweet+="\n"
	else:
		inurl = "http://54.212.247.174:8983/solr/pingher_nort/select?q="+urllib2.quote(string)+"&wt=json"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		tweet = (docs[0]['tweet_text'][0])
	return tweet
