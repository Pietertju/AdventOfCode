from copy import deepcopy

def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [line.strip() for line in file.read().split("\n")]

    values = {}
    operations = {}

    readingStart = True
    for line in lines:
        if len(line) == 0:
            readingStart = False
            continue

        if readingStart:
            splitString = line.split(":")
            value = True if int(splitString[1].strip()) == 1 else False 
            key = splitString[0].strip()
            values[key] = value

        else:
            splitString = line.split("->")
            rightPart = splitString[1].strip()
            leftSplit = splitString[0].strip().split()
            a = leftSplit[0].strip()
            operation = leftSplit[1].strip()
            b = leftSplit[2].strip()
            operations[rightPart] = (a, operation, b)
    
    return values, operations

def getWireCalc(values, operations, wire):
    (a, operation, b) = operations[wire]
    if not (a in values):
        getWireCalc(values, operations, a)
    if not (b in values):
        getWireCalc(values, operations, b)

    aValue = values[a]
    bValue = values[b]

    if operation == "OR":
        values[wire] = aValue | bValue
    elif operation == "XOR":
        values[wire] = aValue ^ bValue
    elif operation == "AND":
        values[wire] = aValue & bValue
    else:
        print("wtf")


def partOne(values, operations):
    zValues = []

    for wire in operations:
        if wire.startswith('z'):
            (a, operation, b) = operations[wire]
            getWireCalc(values, operations, wire)
            zValues.append(wire)

    zValues = sorted(zValues)

    binaryString = ""

    for wire in zValues:
        if values[wire]:
            binaryString += "1"
        else:
            binaryString += "0"
     
    binaryString = binaryString[::-1]
    answer = int(binaryString, 2)

    print("Part One: ", answer)

def partTwo(values, operations):


    print("Part Two: ", 0)

values, operations = getInput()
partOne(deepcopy(values), deepcopy(operations))
