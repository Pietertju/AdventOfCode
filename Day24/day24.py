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
    
    print(a, " ", operation, "  ", b, " -> ", wire)

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

def swapPairs(operations, a, b):
    tempOp = operations[a]
    operations[a] = operations[b]
    operations[b] = tempOp

def partTwo(values, operations):
    swapPairs(operations, "z08", "mvb")
    swapPairs(operations, "rds", "jss")
    swapPairs(operations, "z18", "wss")
    swapPairs(operations, "z23", "bmn")
    for i in range(0, 46):
        if i < 10:
            getWireCalc(values, operations, "z0"+str(i))
        else:
            getWireCalc(values, operations, "z"+str(i))
        print("-----------------------")
        
    wrongThingies = sorted(["z08", "mvb", "rds", "jss", "wss", "z18", "z23", "bmn"])
    for thing in wrongThingies:
        print(thing, end=",")
    print()

    print("Part Two: ", 0)

values, operations = getInput()
#partOne(deepcopy(values), deepcopy(operations))
partTwo(values, operations)
