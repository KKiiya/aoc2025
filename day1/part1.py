testPassComb = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
passComb = []
minThreshold = 0
maxThreshold = 99
position = 50
password = 0

def readFile(file: str):
    with open('c:\\Users\\Alumno\\Documents\\Git\\aoc2025\\day1\\'+file, 'r') as file:
        for line in file:
            passComb.append(line.strip())

def getMovement(inputLine: str):
    if inputLine.startswith("L"):
        return -int(inputLine.replace("L", ""))
    else: return int(inputLine.replace("R", ""))

def stabilize(num):
    newNum = 0
    if num > maxThreshold:
        newNum -= maxThreshold
        stabilize(newNum)
    if num < minThreshold:
        newNum += maxThreshold
        stabilize(newNum)
    return num

def operate(count: int):
    global position
    global password
    position += count
    if position < minThreshold:
        position = stabilize(maxThreshold + (position - minThreshold + 1))
        print(f"Position wrapped below minThreshold: position = {position}")
    elif position > maxThreshold:
        position = stabilize(minThreshold + (position - maxThreshold) - 1)
    if position == 0:
        password += 1
        print("Position pointed at 0. Pointed times: ", password)

def getPassword(combination: list):
    for inputLine in(combination):
        quantity = getMovement(inputLine)
        operate(quantity)


readFile("input.txt")
getPassword(passComb)
print(password)