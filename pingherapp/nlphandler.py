from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from nltk import pos_tag, word_tokenize
from nltk import RegexpParser
from nltk import ne_chunk

def nlp(sentence):

	#sentence = tokenize.sent_tokenize(sentence)
	#sentence = "As you run out of cash, people depending upon cash economy lose their jobs: @meerasanyal #DeMonitisation"
	#print(sentence)
	sid = SentimentIntensityAnalyzer()
	ss = sid.polarity_scores(sentence)
	"""for k in sorted(ss):
	    print('{0}: {1}, '.format(k, ss[k]), end='')"""
	print(ss)
	text = word_tokenize(sentence)
	text = pos_tag(text)
	print(text)
	#grammar = "NP: {<DT>?<JJ>*<NN>}"
	grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
	cp = RegexpParser(grammar)
	result = cp.parse(text)
	print(result)

nlp(input("Enter a tweet"))