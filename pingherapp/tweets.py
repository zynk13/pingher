import urllib2
import json
import os.path


screen_name=""
tweet_data={"tweet_text":"","tweet_url":[]}
	

def process_tweets_from(string,data):
	## Read out positive tweets from dna about demonetization

	if "tweets from" in string.lower() and "sentiment" in data['entities']:
		#screen_name=string.lower().replace("tweets from ","")
		screen_name=data['entities']['tweets_from'][0]['value'].lower().replace("tweets from ","")
		if "question_type" in data['entities'].keys():
			string=string.replace(data['entities']['question_type'][0]['value'].lower(),"")
		if "desc_q" in data['entities'].keys():
			string=string.replace(data['entities']['desc_q'][0]['value'].lower(),"")
		string=string.replace("tweets from ","")
		string=string.replace(screen_name,"")
		flag=-1
		print string
		print screen_name
		if "positive" in string:
			flag=1
			string=string.replace("positive","")
		elif "negative" in string:
			flag=-1
			string=string.replace("negative","")
		elif "neutral" in string:
			flag=0
			string=string.replace("neutral","")
		inurl="http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"%20screen_name:"+urllib2.quote(screen_name)+"&wt=json"
		print inurl
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		max_ind=[];
		pos_score=0.5;
		neg_score=-0.0;
		tweet_list=[]
		if flag==1:
			for i in range(len(docs)):
				if docs[i]['sentiment'][0]>pos_score and docs[i]['tweet_text'][0] not in tweet_list:
					#score=docs[i]['sentiment']
					max_ind.append(i)
					tweet_list.append(docs[i]['tweet_text'][0])
		elif flag==-1:
			for i in range(len(docs)):
				if docs[i]['sentiment'][0]<neg_score and docs[i]['tweet_text'][0] not in tweet_list:
					#score=docs[i]['sentiment']
					max_ind.append(i)
					tweet_list.append(docs[i]['tweet_text'][0])
		elif flag==0:
			for i in range(len(docs)):
				if docs[i]['sentiment'][0]==0.0 and docs[i]['tweet_text'][0] not in tweet_list:
					#score=docs[i]['sentiment']
					max_ind.append(i)
					tweet_list.append(docs[i]['tweet_text'][0])

			print max_ind
		
		size=5
		if len(max_ind)<5:
			size=len(max_ind)
		for i in range(size):
			tweet_data["tweet_text"]+=(docs[max_ind[i]]['tweet_text'][0])
			tweet_data["tweet_text"]+="\n"
			tweet_data["tweet_url"].append(docs[max_ind[i]]['url'])
		if size==0:
			json_val=json.load(open(os.path.join(BASE, "noname.json")))
			tweet_data["tweet_text"]=json_val["NO_NAME"]
		

		
	## Read out tweets from dna
	elif "tweets from" in string.lower():
		screen_name=string.lower().replace("tweets from ","")
		screen_name=screen_name.lower().replace(" ","")
		string=string.replace("tweets from ","")
		string=string.replace(screen_name,"")
		if "question_type" in data['entities'].keys():
			string=string.replace(data['entities']['question_type'][0]['value'].lower(),"")
		if "desc_q" in data['entities'].keys():
			string=string.replace(data['entities']['desc_q'][0]['value'].lower(),"")
		inurl="http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"%20screen_name:"+urllib2.quote(screen_name)+"&wt=json"
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

	return tweet_data



def process_show(string,data):
	## Show me possitive tweets on demonetization
	print string
	if "show" in string.lower():
		string=string.lower().replace("show","")
		flag=0
		if "positive" in string:
			flag=1
			string=string.replace("positive","")
		elif "negative" in string:
			flag=-1
			string=string.replace("negative","")
		elif "neutral" in string:
			flag=0
			string=string.replace("neutral","")
		inurl = "http://54.212.247.174:8983/solr/pingher/select?q="+urllib2.quote(string)+"&rows=100&wt=json"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		max_ind=[];
		pos_score=0.3;
		neg_score=-0.3;
		screen_name_list=[]
		tweet_list=[]
		if flag==1:
			for i in range(len(docs)):
				if docs[i]['sentiment'][0]>pos_score and docs[i]['screen_name'] not in screen_name_list and docs[i]['tweet_text'][0] not in tweet_list:
					#score=docs[i]['sentiment']
					max_ind.append(i)
					screen_name_list.append(docs[i]['screen_name'][0])
					tweet_list.append(docs[i]['tweet_text'][0])
		elif flag==-1:
			for i in range(len(docs)):
				if docs[i]['sentiment'][0]<neg_score and docs[i]['screen_name'] not in screen_name_list  and docs[i]['tweet_text'][0] not in tweet_list:
					#score=docs[i]['sentiment']
					max_ind.append(i)
					screen_name_list.append(docs[i]['screen_name'][0])
					tweet_list.append(docs[i]['tweet_text'][0])
		elif flag==0:
			for i in range(len(docs)):
				if docs[i]['sentiment'][0]==0 and docs[i]['screen_name'] not in screen_name_list  and docs[i]['tweet_text'][0] not in tweet_list:
					#score=docs[i]['sentiment']
					max_ind.append(i)
					screen_name_list.append(docs[i]['screen_name'][0])
					tweet_list.append(docs[i]['tweet_text'][0])
		

		#max_ind=sorted(max_ind)
		size=5
		if len(max_ind)<5:
			size=len(max_ind)
		for i in range(size):
			tweet_data["tweet_text"]+=(docs[max_ind[i]]['tweet_text'][0])
			tweet_data["tweet_text"]+="\n"
			tweet_data["tweet_url"].append(docs[max_ind[i]]['url'])
		if size==0:
			json_val=json.load(open(os.path.join(BASE, "noname.json")))
			tweet_data["tweet_text"]=json_val["NO_NAME"]
		
		return tweet_data
