def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [list(line.strip()) for line in file.read().split("\n")]

    keys = []
    locks = []

    grid = []

    newGrid = True
    isLock = False

    for line in lines:
        if newGrid:
            isLock = True
            for i in line:
                if i != '#':
                    isLock = False
                    break
            newGrid = False
                
        if len(line) == 0:
            newGrid = True
            if isLock:
                locks.append(grid)
            else:
                keys.append(grid)
            grid = []
            continue
        grid.append(line)

    return keys, locks

def prettyPrintGrid(grid):
    print()
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            print(c, end="")
        print()

def partOne(keys, locks):
    answer = 0

    for key in keys:
        for lock in locks:
            keyLenghts = []
            lockLenghts = []
            
            locksFit = True
           
            #print(len(key), "  -  ", len(lock))
            #print(len(key[0]), "  -  ", len(lock[0]))

            for y in range(len(lock[0])):
                keyLen = 0
                lockLen = 0
                for x in range(len(lock)):
                    if lock[x][y] == '#':
                        lockLen += 1
                    if key[x][y] == '#':
                        keyLen += 1
                keyLenghts.append(keyLen)
                lockLenghts.append(lockLen)
                if keyLen + lockLen > len(lock):
                    locksFit = False
                    break
            
            if locksFit:
                answer += 1
    print("Part OneL: ", answer)

keys, locks = getInput()

partOne(keys, locks)