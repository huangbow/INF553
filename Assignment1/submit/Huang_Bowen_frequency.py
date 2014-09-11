from __future__ import division
import sys
import json
import string


def main():
	tweet_file=open(sys.argv[1])
	term_in_tweet={}
	term_freq={}

	#get each term
	for line in tweet_file:
		decode=json.loads(line)
		if "en"==decode["lang"]:
			v_word=decode["text"].split()
			for word in v_word:
				word=word.lower()
				word=word.encode('utf-8').translate(None, string.punctuation)
				if term_in_tweet.get(word)!=None:
					term_in_tweet[word]+=1#count the term
				else:
					term_in_tweet[word]=1#first time get this term
	#print term_in_tweet.items()
	#end-----get each term


	num_of_words=0
	num_of_terms=0

	for k,v in term_in_tweet.items():
		num_of_words+=int(v)
		num_of_terms+=1
	for k,v in term_in_tweet.items():
		num_up=v/num_of_words
		#num_down=v/num_of_terms
		#print num_down

		#an interesting way to count freq
		#print num_up/num_down

		#the assign way
		term_freq[k]=num_up


	#print term_freq.items()
	for k,v in term_freq.items():
		print str(k)+"\t"+str(v)


if __name__ == '__main__':
    main()