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
		for key in intermediateDicForPass[0]:
			a.append(key)
		temp_candi=set(itertools.combinations(a, size))
		candiSet=temp_candi

		# for candi in temp_candi.copy():
		# 	for s in intermediateSetForPass[size-2]:
		# 		if (s in set(candi))==False:
		# 			if size==2:
		# 				print (s in set(candi))
		# 				print s,set(candi),"dif"
		# 			candiSet.discard(candi)
		candiSet=temp_candi

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

	print intermediateDicForPass


def main():
	data=open(sys.argv[1])
	support=sys.argv[2]

	Apriori(data,support)


if __name__ == '__main__':
	main()