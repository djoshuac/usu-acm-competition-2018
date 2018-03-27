import random
from datetime import datetime
random.seed(datetime.now())

start = int(input("start: "))
stop = int(input("stop: "))
pre = "test"

wordBank = ["hi", "bye", "food", "water", "can", "oClock", 're-do', "money", "voice", "candy", "cookie",
            "big", "empire", "alternative", "snake", "bananas", "mississippi", "drump", "candidate",
            "running", "egg", "cooking", "monkey", "sing", "bunny", "hyperactive", "excessive", "alternate"]

for i in range(start, stop + 1):
    with open(pre + str(i) + ".txt", 'w') as file:
        line = random.randrange(0, 1000)
        file.write(str(line) + "\n")
        for _ in range(line):
            wc = random.randrange(4, 13)
            for x in range(wc):
                file.write(random.choice(wordBank))
                if x == (wc-1):
                    file.write("?\n")
                else:
                    file.write(" ")