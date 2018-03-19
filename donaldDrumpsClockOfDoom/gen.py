import random
from datetime import datetime
random.seed(datetime.now())
toGen = int(input("How many test cases to generate: "))
testPre = "test"

for i in range(toGen):
    with open(testPre+str(i)+".txt", 'w') as file:
        for _ in range(16):
            file.write("{:02d}{:02d}\n".format(random.randrange(0, 24), random.randrange(0, 60)))