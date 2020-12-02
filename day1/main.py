

def readFile():
    file = open("input.txt","r")
    numList = []
    for i in file.readlines():
        numList.append(int(i[0:-1]))

    return numList

def partOne():
    numList = readFile()
    goal = 2020
    for a in numList:
        for b in numList:
            if a + b == goal:
                print(a*b)


def partTwo():
    numList = readFile()
    goal = 2020
    for a in numList:
        for b in numList:
            for c in numList:
                if a + b + c == goal:
                    print(a*b*c)
                    return


#partOne()
partTwo()
        
