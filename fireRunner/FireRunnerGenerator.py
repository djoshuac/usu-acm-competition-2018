
from random import randint

def main():
	n = 47
	file = open("input1.txt", "w")
	file.write(str(n))
	file.write("\n")
	
	middle = (n-1)/2
	
	for y in xrange(n):
		for x in xrange(n):
			if abs(x-middle) + abs(y-middle) > middle:
				file.write("0")
			else:
				file.write(str(randint(1, 1000)))
			if x != n-1:
				file.write(" ")
			
		if y != n-1:
			file.write("\n")
	
	file.close()
	
if __name__ == '__main__':
	main()