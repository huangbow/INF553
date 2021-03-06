import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(record):
	key=record[0]
	value=record[1]
	h=hash(value)
	#remove last 10 letters
	value=value[:-10]
	mr.emit_intermediate(h,value)


def reducer(key,list_of_value):
	#guarantee that if it duplicates, only output one
	mr.emit(list_of_value[0])


if __name__ == '__main__':
	inputdata=open(sys.argv[1])
	mr.execute(inputdata,mapper,reducer)