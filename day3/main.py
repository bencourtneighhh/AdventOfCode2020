def readFile(): # Reads the input as stores into an array
    file = open("input.txt","r")
    slope = []
    for i in file.readlines():
        slope.append(i[0:-1])

    return slope


def main(addPos):


    slope = readFile()
    currentPos = [0,0]
    treeCount = 0
    
    while currentPos[0] < len(slope) - 1 :
        # Current pos is moved, and index decreased if necessary to count for the looping of the map
        currentPos[1] =  (currentPos[1] + addPos[1]) % len(slope[0])
        currentPos[0] +=  addPos[0] # Map is not vertically infinite

        if slope[currentPos[0]][currentPos[1]] == "#":
            treeCount += 1

    return treeCount

def partOne():
    print(main ([1,3]))

def partTwo():
    total = main([1,1]) * main([1,5]) * main([1,3]) * main([1,7]) * main([2,1])
    print(total)

#partOne()

partTwo()
