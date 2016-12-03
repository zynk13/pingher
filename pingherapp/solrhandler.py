import urllib2
import json
import os.path

def solrcall(string):
	
	#Getting SOLR Hosted URL and docs
	screen_name=""
	tweet_data={"tweet_text":"","tweet_url":[]}
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
			tweet_data["tweet_text"]+=(docs[i]['tweet_text'][0])
			tweet_data["tweet_text"]+="\n"
		if size==0:
			json_val=json.load(open(os.path.join(BASE, "noname.json")))
			tweet_data["tweet_text"]=json_val["NO_NAME"]
	else:
		inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"&wt=json"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		tweet_data["tweet_text"] = (docs[0]['tweet_text'][0])
		tweet_data["tweet_url"] = (docs[0]['url'])
	print tweet_data
	return tweet_data
