import os

directory = os.getcwd()+"\\day2\\"
testIDS = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]
ids = []

with open(directory+"input.txt") as file:
    for line in file: 
        for availableID in line.split(","): ids.append(availableID)

def getRange(listId: str) -> list:
    return listId.split("-")

def isValidId(validatedId: str) -> bool:
    length = len(validatedId)

    for sequence in range(1, length // 2 + 1):
        if length % sequence == 0:
            seq = validatedId[:sequence]
            repetitions = length // sequence

            if seq * repetitions == validatedId: return True
    return False 

def getInvalidIds(idsRangeList: list) -> int:
    invalidIds = 0

    for listId in idsRangeList:
        idRange = getRange(listId)
        initial = int(idRange[0])
        final = int(idRange[1])

        for i in range(initial, final, 1):
            if not isValidId(str(i)): invalidIds += 1
                
    return invalidIds


print(getInvalidIds(ids))