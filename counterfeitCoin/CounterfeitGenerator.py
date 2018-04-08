



if __name__ == '__main__':
	from random import randint

	file = open("input1.txt", "w")
	
	t = 250
	file.write(str(t))
	
	for x in xrange(t):
		file.write("\n")
		file.write(str(randint(1, 100000)))
	
	file.close()