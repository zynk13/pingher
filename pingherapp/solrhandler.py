import urllib2
import json
import os.path
import tweets

def solrcall(string,data):
	
	#Getting SOLR Hosted URL and docs
	screen_name=""
	tweet_data={"tweet_text":"","tweet_url":[],"media_url":[]}
	string=string.lower()
	#print string
	if "stat" in data['entities']:
		if "demonetization" in data['entities']:
			string=data['entities']['demonetization'][0]["value"];
			inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(data['entities']['demonetization'][0]["value"])+"&wt=json&rows=1000"
		elif "target_person" in data['entities']:
			string=data['entities']['target_person'][0]["value"];
			inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(data['entities']['target_person'][0]["value"])+"&wt=json&rows=1000"
		print inurl
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		pos=0.0
		neg=0.0
		neu=0.0
		print len(docs)
		for i in range(len(docs)):
			#print docs[i]['sentiment'][0]
			if docs[i]['sentiment'][0]>0.0:
				pos+=1
			elif docs[i]['sentiment'][0]<0.0:
				neg+=1
			elif docs[i]['sentiment'][0]==0.0:
				neu+=1
		tweet_data["tweet_text"]=str(pos*100/len(docs))+" percentage of general public are happy ,"+str(neg*100/len(docs))+" percentage of general public are sad and "+str(neu*100/len(docs))+" percentage of general public are neutral about "+string


	elif "show" in string:
		tweet_data=tweets.process_tweets_from(string,data)

	else:
		inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"&wt=json&rows=100"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		size=5
		if "image" in string:
			size=4
		for i in range(size):
			tweet_data["tweet_text"]+=(docs[i]['tweet_text'])
			tweet_data["tweet_text"]+="\n"
			if "media_url" in docs[i]:
				tweet_data["media_url"].append(str(docs[i]['media_url'][0]))
			elif "url" in docs[i].keys():
				tweet_data["tweet_url"].append(docs[i]['url'])

	#print tweet_data
	return tweet_data
