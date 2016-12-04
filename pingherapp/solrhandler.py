import urllib2
import json
import os.path
import tweets

def solrcall(string,data):
	
	#Getting SOLR Hosted URL and docs
	screen_name=""
	tweet_data={"tweet_text":"","tweet_url":[]}
	string=string.lower()
	print string
	if "tweets from" in string:
		tweet_data=tweets.process_tweets_from(string,data)
	elif "show" in string:
		tweet_data=tweets.process_show(string,data)
			
	else:
		inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"&wt=json"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		tweet_data["tweet_text"] = (docs[0]['tweet_text'][0])
		tweet_data["tweet_url"] = (docs[0]['url'])
	print tweet_data
	return tweet_data
