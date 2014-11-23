import sys
import itertools

items=[]
supportDic={}
#contain 
intermediateDicForPass=[]
intermediateSetForPass=[]

pair=set()


def countSupport(valueList):
	for value in valueList:
		for w in value:
			if supportDic.get(w)==None:
				supportDic[w]=1
			else:
				supportDic[w]+=1

def deleNonFreqItem(valueDic,support):
	intermediateDicForPass1={}
	intermediateSetForPass1=set()
	for k in valueDic:
		if int(valueDic.get(k))-int(support)>=0:
			intermediateDicForPass1[k]=valueDic[k]
			intermediateSetForPass1.add(k)
	intermediateDicForPass.append(intermediateDicForPass1)
	intermediateSetForPass.append(intermediateSetForPass1)

def pass1(data,support):
	for line in data:
		#del '\n';split by ','
		#set items to by 2D list
		#each row is a SET
		items.append(set(line.rstrip('\n').split(',')))
		#get Lexicographic ordering 
	countSupport(items)
	deleNonFreqItem(supportDic,support)
	
	# print "frequent itemsets of size 1:"
	# for k in intermediateDicForPass1:
	# 	print k,intermediateDicForPass1[k]

def Apriori(data,support):
	size=1
	for line in data:
		#del '\n';split by ','
		#set items to by 2D list
		#each row is a SET
		items.append(set(line.rstrip('\n').split(',')))
		#get Lexicographic ordering 
	countSupport(items)
	deleNonFreqItem(supportDic,support)


	size=size+1
	while(len(intermediateSetForPass[size-2])>=size):
		print len(intermediateSetForPass[size-2])
		a=[]
		candiSet=set()
		for key in supportDic:
			a.append(key)
		temp_candi=set(itertools.combinations(a, size))
		# candiSet=temp_candi
		if size==4:
			print temp_candi,"candi"
		for candi in temp_candi:
			for s in intermediateSetForPass[size-2]:
				if size==4:
					print set(s).issubset(set(candi))
				if set(s).issubset(set(candi))==False:
					candiSet.add(candi)
		if size==4:
			print candiSet
		temp_dicForPassK={}
		intermediateDicForPassK={}
		intermediateSetForPassK=set()
		for candi in candiSet:
			for setForEachRow in items:
				if set(candi).issubset(setForEachRow):
					if temp_dicForPassK.get(candi)==None:
						temp_dicForPassK[candi]=1
					else:
						temp_dicForPassK[candi]+=1
		for key in temp_dicForPassK:
			if int(temp_dicForPassK[key])-int(support)>=0:
				intermediateDicForPassK[key]=temp_dicForPassK[key]
				intermediateSetForPassK.add(key)
		intermediateDicForPass.append(intermediateDicForPassK)
		intermediateSetForPass.append(intermediateSetForPassK)
		size+=1
		
		
	#--------------------while END-------------------------------------------

	# print intermediateDicForPass
	
		


def pass2(support):
	#generate pairs
	a=[]
	for key in supportDic:
		a.append(key)
	temp_pair=set(itertools.combinations(a, 2))
	# generate pair if freq size 1 contain the subset
	for p in temp_pair:
		if set(p).issubset(intermediateSetForPass[0])==True:
			pair.add(p)

	intermediateDicForPass2={}
	for k in pair:
		for setForEachRow in items:
			if set(k).issubset(setForEachRow):
				if intermediateDicForPass2.get(k)==None:
					intermediateDicForPass2[k]=1
				else:
					intermediateDicForPass2[k]+=1
	for key in intermediateDicForPass2:
		if int(intermediateDicForPass2[key]-int(support))>=0:
			print key,intermediateDicForPass2[key]

def passk(data,support):
	pass1(data,support)
	pass2(support)
	a=[]
	b=[]
	# for key in intermediateDicForPass1:
	# 	a.append(key)
		# test=test.union(set([key]))
	# for i in test:
	# 	print i
	# print list(itertools.combinations(a, 3))



def main():
	data=open(sys.argv[1])
	support=sys.argv[2]
	# pass1(data,support)
	# pass2(support)
	# passk(data,support)
	Apriori(data,support)


if __name__ == '__main__':
	main()