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
    password = 0

    for inputLine in combination:
        movement = getMovement(inputLine)
        prePosition = position + movement
        position = prePosition % (maxThreshold + 1)
        
        if movement < 0:

        else:
            
    return password

print(getPassword(testPassComb))