def lines(fp):
    print str(len(fp.readlines()))
def main():
    scores={}
    sent_file = open("AFINN-111.txt")
    for line in sent_file:
    	term, score = line.split('\t')
        scores[term]=int(score)
    print scores.items()

if __name__ == '__main__':
    main()