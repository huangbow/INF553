import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(record):
	key=record[0]
	value=record[1]
	#get a unique k for each pair
	k=hash(key)+hash(value)
	mr.emit_intermediate(k,(key,value))

def reducer(key,list_of_value):
	total=0
	for v in list_of_value:
		total+=1
	if total==1:
		for v in list_of_value:
			mr.emit((v[0],v[1]))
			mr.emit((v[1],v[0]))

if __name__ == '__main__':
	inputdata=open(sys.argv[1])
	mr.execute(inputdata,mapper,reducer)