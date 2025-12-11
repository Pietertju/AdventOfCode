

def partOne():
    answer = 0
    
    lines = []
    with open("input.txt") as file:
        input = file.read()
        lines = input.split("\n")

    instructions = [int(line[1:]) for line in lines]
    directions = [True if line[0] == 'R' else False for line in lines]

    startIndex = 50

    for index in range(0, len(instructions)):
        if directions[index]:
            startIndex += instructions[index]
        else:
            startIndex -= instructions[index]

        while startIndex < 0:
            startIndex = 100 + startIndex

        while startIndex > 99:
            startIndex = startIndex - 100

        if startIndex == 0:
            answer += 1
    print("Part one: ", answer)

def partTwo():
    answer = 0
    
    lines = []
    with open("input.txt") as file:
        input = file.read()
        lines = input.split("\n")

    instructions = [int(line[1:]) for line in lines]
    directions = [True if line[0] == 'R' else False for line in lines]

    startIndex = 50
    previousIndex = 50
    for index in range(0, len(instructions)):
        if directions[index]:
            startIndex += instructions[index]
        else:
            startIndex -= instructions[index]

        skip = False
        while startIndex > 99:
            startIndex = startIndex - 100
            answer += 1
            skip = True

        if skip:
            previousIndex = startIndex
            continue

        while startIndex < 0:
            if previousIndex != 0:
                answer += 1
            startIndex = 100 + startIndex
            previousIndex = startIndex

        if startIndex == 0:
            answer += 1
        previousIndex = startIndex
    print("Part two: ", answer)


partOne()
partTwo()