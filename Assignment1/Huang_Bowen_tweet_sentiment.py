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
        #json-->dictionary
        decode=json.loads(line)
        # decode1=json.dumps(line)
        #print decode
        #dict ergodic
        # for key,val in scores.items():#words_file
        #     for k,v in decode.items():#twitter_file
        #         v_word=str(v).split(' ')#split sentence into words
        #         # print v_word
        #         for word in v_word:    
        #             str_exist=str(word).find(key)#whether words in twitter_file contains any words
        #             if str_exist>-1:
        #                 if len(str(word))-len(key)<=2:#make sure the word is exactly the word, rather than a slice
        #                     num_sum+=int(val)
        #                     # print word
        #                     # print v_word
        #                     # print key
        # for k,v in decode.items():
        #     print k
        v_word=decode["text"].split()
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
