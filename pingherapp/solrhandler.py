import urllib2
import json
import os.path
import tweets

def solrcall(string,data):
	
	#Getting SOLR Hosted URL and docs
	screen_name=""
	tweet_data={"tweet_text":"","tweet_url":[]}
	string=string.lower()
	#print string
	if "show" in string:
		tweet_data=tweets.process_tweets_from(string,data)
			
	else:
		inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"&wt=json&rows=100"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		#tweet_data["tweet_text"] = (docs[0]['tweet_text'])
		#if "url" in docs[0].keys():
		#	tweet_data["tweet_url"] = (docs[0]['url'])
		size=5
		for i in range(size):
			tweet_data["tweet_text"]+=(docs[i]['tweet_text'])
			tweet_data["tweet_text"]+="\n"
			if "media_url" in docs[i]:
				tweet_data["tweet_url"].append(docs[i]['media_url'])
			elif "url" in docs[i].keys():
				tweet_data["tweet_url"].append(docs[i]['url'])

	#print tweet_data
	return tweet_data
