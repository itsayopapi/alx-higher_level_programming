#!/usr/bin/python3
import sys
if __name__=="__main__":
	ag = len(sys.argv)
	if ag <= 1:
		print("{:d} arguments".format(ag - 1))
	else:
		print("{:d} arguments".format(ag - 1))
		for i in range(ag):
			if i != 0:
				print("{:d}: {}".format((i), sys.argv[i]))
