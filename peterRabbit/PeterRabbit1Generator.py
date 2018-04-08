# Peter Rabbit p1 generator

from random import randint


def tunnel_gen(n, m, total_dist):
	
	for ind in xrange(m):
		v1 = randint(1, n)
		v2 = randint(1, n)
		while v1 == v2:
			v2 = randint(1, n)
		
	
		yield [str(min(v1, v2)), str(max(v1, v2)), str(randint(1, total_dist))]
	

def main():
	n = 20 #farms
	m = 350
	
	file = open("input1.txt", "w")
	file.write("".join([str(n), " ", str(m), "\n"]))
	
	sumVal = 0
	for i in xrange(n - 1):
		val = randint(1, 1000)
		sumVal += val
		file.write(str(val))
		if i != n-2:
			file.write(" ")
	
	
	gen = tunnel_gen(n, m, sumVal)
	
	for i in gen:
		file.write("\n")
		file.write(" ".join(i))
	

	file.close()


	
if __name__ == '__main__':
	main()