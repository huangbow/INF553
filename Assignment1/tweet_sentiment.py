import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = {}
    for line in sent_file:
    	term, score = line.split('\t')
    	scores[term] = int(score)
    print scores.items()

if __name__ == '__main__':
    main()
