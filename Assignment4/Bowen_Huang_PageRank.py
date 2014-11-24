from __future__ import division
import sys

inputMatrix=[]
initialM=[]
matrixA=[]


def matrixMultiple(mA,mB):
	size=len(mA)
	temp=0
	tempMatrix=[]
	for i in range(0,size):
		tempMatrix.append([0])

	#rows of A
	for i in range(0,size):
		#columns of B
		for j in range(0,len(mB[0])):
			#rows of B
			for k in range(0,len(mB)):
				tempMatrix[i][j]+=mA[i][k]*mB[k][j]
	return tempMatrix



#return the number of the nodes
def initializeInputMatrix(data):
	for line in data:
		inputMatrix.append([int(n) for n in line.split()])
	#every Row means OutReachDegree of the node of it
	#sumOfRow means the sum of ORD
	sumOfRow=[]
	for x in inputMatrix:
		tempSum=0
		for y in x:
			tempSum+=y
		sumOfRow.append(tempSum)
	#initialize M_initial
	size=len(sumOfRow)
	for i in xrange(0,size):
		initialM.append([int(0) for n in xrange(0,size)])
	
	for x in xrange(0,size):
		for y in xrange(0,size):
			if inputMatrix[x][y]==1:
				initialM[y][x]=1/sumOfRow[x]
	# print initialM
	return len(initialM)


def geneMatrixA(beta,size):
	val=(1-float(beta))/size
	for x in xrange(0,size):
		matrixA.append([0 for n in xrange(0,size)])
	
	for x in range(0,size):
		for y in range(0,size):
			matrixA[x][y]=float(beta)*float(initialM[x][y])+float(val)
	# print matrixA


def iteration(numItaration,size):
	val=1/size
	matrixROld=[]
	for i in range(0,size):
		matrixROld.append([val])
	print len(matrixROld[0])
	for i in range(0,numItaration):
		matrixROld=matrixMultiple(matrixA,matrixROld)



	print matrixROld




def main():
	data=open(sys.argv[1])
	numItaration=sys.argv[2]
	beta=sys.argv[3]
	size=initializeInputMatrix(data)
	geneMatrixA(beta,size)
	iteration(int(numItaration),size)



if __name__ == '__main__':
	main()