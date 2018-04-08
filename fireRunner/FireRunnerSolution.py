
def getMaxPath(posX, posY, start, house, houseMap):
	if posX + posY * len(house) in houseMap:
		return houseMap[posX + posY * len(house)]
	if abs(posX - start) + abs(posY - start) == start:
		return house[posY][posX]
		
	
	distance = abs(posX - start) + abs(posY - start)
	
	up = abs(posX - start) + abs((posY - 1) - start)
	down = abs(posX - start) + abs((posY + 1) - start)
	left = abs((posX - 1) - start) + abs(posY - start)
	right = abs((posX + 1) - start) + abs(posY - start)
	
	bestPath = 0
	
	if up > distance:
		bestPath = max(bestPath, getMaxPath(posX, posY-1, start, house, houseMap))
	if down > distance:
		bestPath = max(bestPath, getMaxPath(posX, posY+1, start, house, houseMap))
	if left > distance:
		bestPath = max(bestPath, getMaxPath(posX-1, posY, start, house, houseMap))
	if right > distance:
		bestPath = max(bestPath, getMaxPath(posX+1, posY, start, house, houseMap))
		
	houseMap[posX + posY * len(house)] = bestPath + house[posY][posX]
	return houseMap[posX + posY * len(house)]


size = int(raw_input())

house = []
houseMap = {}

for x in xrange(size):
	arr = [int(x) for x in raw_input().split(" ")]
	house.append(arr)
	
start = (size - 1)/2

print(getMaxPath(start, start, start, house, houseMap))