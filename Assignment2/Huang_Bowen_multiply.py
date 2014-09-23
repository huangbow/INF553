import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(record):
	#get matrix, string
	key=record[0]
	#get i
	x=record[1]
	#get j
	y=record[2]
	#get value
	val=record[3]
	for k in range(5):
		if key=="a":
			mr.emit_intermediate((x,k),(key,y,val))
		elif key=="b":
			mr.emit_intermediate((k,y),(key,x,val))

def reducer(key,list_of_value):
	#store the list of the row in matrix A
	a_elm=[]
	#store the list of the column in matrix B
	b_elm=[]
	#the value of (i,k) in the solution of A(i,j)*B(j,k)
	total=0
	for v in list_of_value:
		if v[0]=="a":
			a_elm.append((v[1],v[2]))
		elif v[0]=="b":
			b_elm.append((v[1],v[2]))
	for a in a_elm:
		for b in b_elm:
			if a[0]==b[0]:
				total+=a[1]*b[1]
	mr.emit((key,total))


if __name__ == '__main__':
	inputdata=open(sys.argv[1])
	mr.execute(inputdata,mapper,reducer)