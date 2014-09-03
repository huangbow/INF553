import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} #initial dictionary
    for line in sent_file:
        line=line.lower() #make every letter is lower one
    	term, score = line.split('\t')
    	scores[term] = int(score)
    #print scores.items()

    #tweet_file
    for line in tweet_file:
        num_sum=0
        #json-->dictionary
        decode=json.loads(line)
        v_word=decode["text"].split()#find the value of key"text"
        for key,val in scores.items():
            for word in v_word:
                word=word.lower()
                uni_word = word.encode('utf-8').translate(None, string.punctuation)#Remove ASCII punctuation from your Unicode string
                if uni_word.find(key)>-1:
                    if len(uni_word)-len(key)<1:#uni_word==key
                        num_sum+=int(val)
        print num_sum
if __name__ == '__main__':
    main()
