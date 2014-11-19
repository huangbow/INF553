import sys

items=[]
supportDic={}
intermediateDicForPass1={}
pair={}
paircount={}


def countSupport(valueList):
	for value in valueList:
		for w in value:
			if supportDic.get(w)==None:
				supportDic[w]=1
			else:
				supportDic[w]+=1

def deleNonFreqItem(valueDic,support):
	for k in valueDic:
		if int(valueDic.get(k))-int(support)>=0:
			intermediateDicForPass1[k]=valueDic[k]


def pass1(data,support):
	for line in data:
		#del '\n';split by ','
		#set items to by 2D list
		items.append(line.rstrip('\n').split(','))
		#get Lexicographic ordering 
	countSupport(items)
	deleNonFreqItem(supportDic,support)
	
	print "frequent itemsets of size 1:"
	for k in intermediateDicForPass1:
		print k,intermediateDicForPass1[k]
	


def pass2(support):
	# print items
	#generate pairs
	for k in intermediateDicForPass1:
		pair.setdefault(k,[])
		for v in intermediateDicForPass1:
			if k!=v and pair.get(v)==None:
				pair[k].append(v)
	# print pair
	for k in pair:
		for value in items:
			if k in value:
				for w in pair[k]:
					if w in value:
						if paircount.get((k,w))==None:
							paircount[(k,w)]=1
						else:
							paircount[(k,w)]+=1
	# print paircount
	print "frequent itemsets of size 2:"
	for k in paircount:
		if int(paircount.get(k))-int(support)>=0:
			print k,paircount[k]





def main():
	data=open(sys.argv[1])
	support=sys.argv[2]
	pass1(data,support)
	pass2(support)


if __name__ == '__main__':
	main()