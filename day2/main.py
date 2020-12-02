def readFile(): # Reads the input as stores into an array
    file = open("input.txt","r")
    passList = []
    for i in file.readlines():
        passList.append(i[0:-1])

    return passList

def splitPassword(password):
    # Takes a password and splits it into
    #(lowerBound, upperBound, letter, password)
    
    splitString = password.split(':') # Separates the password and the security rule
    password = splitString[1][1:] # Gets rid of leading whitespace
    
    rule = splitString[0].split(' ') # Splits the count and letter
    letter = rule[1] # Letter to be used in the password

    bounds = rule[0].split('-') # Splits the bounds into lower and upper
    lowerBound = int(bounds[0])
    upperBound = int(bounds[1])
    return lowerBound, upperBound, letter, password

def checkPasswordPartOne(lowerBound, upperBound, letter, password):
    # Checks if the password is valid
    # If it contains between the lower bound and upper bound amount
    # Of the letter within the password, it is valid

    letterCount = 0
    for i in password:
        if i == letter:
            letterCount += 1 

    if letterCount >= lowerBound and letterCount <= upperBound:
        return True # The password is valid

    else:
        return False # The password is not valid

def checkPasswordPartTwo(lowerBound, upperBound, letter, password):
    # Must contain exactly one instance of letter
    # Between the lower and upper bounds indexed of the password
    

    letterCount = 0
    if password[lowerBound - 1] == letter:
        letterCount += 1
    if password[upperBound - 1] == letter:
        letterCount += 1

    if letterCount == 1:
        return True

    else:
        return False


def main():
    part = 2 # Part 1 or 2 to run the specific code
    passList = readFile()
    correctPasswords = 0
    for i in passList:
        x = splitPassword(i)
        if part == 1:
            if(checkPasswordPartOne(*x)):
                correctPasswords += 1
        elif part == 2:
            if(checkPasswordPartTwo(*x)):
                correctPasswords += 1

    print(correctPasswords)

main()
