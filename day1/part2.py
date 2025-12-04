import os

directory = os.getcwd()+"\\day1\\"
testPassComb = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
passComb = []
maxThreshold = 99
startPosition = 50

with open(directory+'input.txt', 'r') as file:
    for line in file: passComb.append(line.strip())
    
def getMovement(inputLine: str):
    if inputLine.startswith("L"): return -int(inputLine.replace("L", ""))
    else: return int(inputLine.replace("R", ""))

def getPassword(combination: list):
    position = startPosition
    print("The dial starts by pointing at", position)
    password = 0
    for inputLine in combination:
        movement = getMovement(inputLine)

        if movement < 0:
            for i in range(abs(movement)):
                position -= 1
                
                if position < 0: position = maxThreshold
                if position == 0: password += 1
        else:
            for i in range(movement):
                position += 1

                if position > maxThreshold:
                    password += 1
                    position = 0
        
        #print("The dial is rotated", inputLine, "to point at", position)
    return password

print(getPassword(passComb))