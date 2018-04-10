farms, tunnels = raw_input().split(' ')
farms = int(farms)
tunnels = int(tunnels)

road = [0]

distances = raw_input().split(' ')

for distance in distances:
    road.append(int(distance) + road[-1])

bestDistance = road[-1]    

for index in xrange(tunnels):
    tunnel = raw_input().split(' ')
    i = int(tunnel[0])
    j = int(tunnel[1])
    d = int(tunnel[2])
    newDistance = road[-1] - road[j-1] + d + road[i-1]
    bestDistance = min(newDistance, bestDistance)

print bestDistance
    