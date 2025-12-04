import os

directory = os.getcwd()+"\\day2\\"
testIDS = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]
ids = []

with open(directory+"input.txt") as file:
    for line in file: 
        for availableID in line.split(","): ids.append(availableID)

def getRange(listId: str) -> list:
    return listId.split("-")

def getInvalidIds(idsRangeList: list) -> int:
    invalidIds = 0

    for listId in idsRangeList:
        idRange = getRange(listId)
        initial = int(idRange[0])
        final = int(idRange[1])

        for i in range(initial, final+1, 1):
            if not (i > final):
                s1 = str(i)
                s2, s3 = s1[:len(s1)//2 + len(s1)%2], s1[len(s1)//2 + len(s1)%2:]
                if s2 == s3: invalidIds+=int(s1)
    return invalidIds


print(getInvalidIds(ids))