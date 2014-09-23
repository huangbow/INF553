import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(record):
	key=record[0]
	x=record[1]
	y=record[2]
	val=record[3]
	h=hash(x)+hash(y)
	mr.emit_intermediate(h,(x,y,val))

def reducer(key,list_of_value):
	

if __name__ == '__main__':
	inputdata=open(sys.argv[1])
	mr.execute(inputdata,mapper,reducer)