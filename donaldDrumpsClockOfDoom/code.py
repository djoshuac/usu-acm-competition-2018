
def getDigit():
    vals = [input() for _ in range(4)]
    hrs, min = sum([int(x[:2]) for x in vals])%24, sum([int(x[2:]) for x in vals])%60
    tmp = (hrs + min) % 42
    while(tmp >= 10):
        tmp = int(str(tmp)[0]) + int(str(tmp)[1])
    return tmp

if __name__ == "__main__":
    print(str(getDigit()) + str(getDigit()) + str(getDigit()) + str(getDigit()))