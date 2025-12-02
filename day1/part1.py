testPassComb = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
passComb = []
minThreshold = 0
maxThreshold = 99
startPosition = 50

def readFile(file: str):
    with open('D:\\Documentos\\GitHub\\aoc2025\\day1\\'+file, 'r') as file:
        for line in file:
            passComb.append(line.strip())

def getMovement(inputLine: str):
    if inputLine.startswith("L"):
        return -int(inputLine.replace("L", ""))
    else: return int(inputLine.replace("R", ""))

def operate(position: int, count: int):
    return (position+count) % (maxThreshold + 1)

def getPassword(combination: list):
    position = startPosition
    password = 0

    for inputLine in combination:
        movement = getMovement(inputLine)
        position = operate(position, movement)
        if position == 0:
            password += 1
    return password


readFile("input.txt")
print(getPassword(passComb))