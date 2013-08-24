#!/usr/bin/python

import sys
#import numpy
import argparse
#from pprint import pprint

def main(args):
	input_file = open(args.file[0])
	for line in input_file:
		spiral = ""
		rows,cols,nums = line.strip().split(";")
		rows = int(rows)
		cols = int(cols)
		nums = nums.split(" ")
		matrix = []

		for i in range(rows):
			row = []
			for j in range(cols):
				row.append(nums[i*cols+j])
			matrix.append(row)
		#matrix = numpy.array(nums)
		#shape = (int(rows), int(cols))
		#matrix = numpy.reshape(matrix, shape)

		#pprint(matrix)

		pop_top = True
		while len(matrix) > 0:
			if pop_top:
				row = matrix.pop(0)
				pop_top = False
			else:
				row = reversed(matrix.pop())
				pop_top = True
			spiral += (" ").join(row)+" "
			matrix = zip(*matrix[::-1])
			#print matrix
		#while  matrix.size > 0:
		#	matrix = matrix.tolist()
		#	row = matrix.pop(0)
		#	spiral += (" ").join(row)+" "
		#	matrix = numpy.array(matrix)
		#	if matrix.size > 0:
		#		matrix = numpy.rot90(matrix)

		print spiral

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("file",nargs=1)
	args = parser.parse_args()
	main(args)
