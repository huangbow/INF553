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
        #newstring = line.encode('utf-8').translate(None, string.punctuation)
        num_sum=0
        decode=json.dumps(line)
        #print decode
        #dict ergodic
        for k,v in scores.items():
            if decode.find(k)>-1:
                num_sum+=v
        print num_sum


if __name__ == '__main__':
    main()
