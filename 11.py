from typing import List
from input_reader import readLines

def part1(xs: List[List[int]]) -> int:
    '''O(steps * nm)'''
    steps = 100
    octStates = xs
    flashes = 0
    for step in range(steps):
        octStates = processStep(octStates)
        flashes += countFlashes(octStates)
    return flashes

def part2(xs: List[List[int]]) -> int:
    '''O(steps * nm)'''
    simulFlashes, target = 0, len(xs) * len(xs[0])
    step = 0
    octStates = xs
    while simulFlashes != target:
        step += 1
        octStates = processStep(octStates)
        simulFlashes = countFlashes(octStates)
    return step

def processStep(xs: List[List[int]]) -> List[List[int]]:
    '''O(nm)'''
    octStates = [ [ xs[row][col] + 1 for col in range(len(xs[0])) ] for row in range(len(xs)) ]
    changes = True
    while changes:
        changes = False
        for row in range(len(xs)):
            for col in range(len(xs[0])):
                if octStates[row][col] > 9:
                    octStates = doFlash(octStates, row, col)
                    changes = True
    return octStates

def validCoord(xs: List[List[int]], row: int, col: int) -> bool:
    '''O(1)'''
    return row >= 0 and row < len(xs) and col >= 0 and col < len(xs[0])

def doFlash(xs: List[List[int]], row: int, col: int) -> List[List[int]]:
    '''O(1)'''
    octStates = xs
    octStates[row][col] = 0
    adjacencies = [ (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i != 0 or j != 0) and validCoord(octStates, row+i, col+j) ]
    for r, c in adjacencies:
        if octStates[row+r][col+c] != 0:
            octStates[row+r][col+c] += 1
    return octStates

def countFlashes(xs: List[List[int]]) -> int:
    '''O(nm)'''
    return sum([ xs[row][col] == 0 for row in range(len(xs)) for col in range(len(xs[0])) ])

def printBoard(xs: List[List[int]]):
    result = "\n".join([ "".join([ str(c) for c in row ]) for row in xs ])
    print(result)

def main():
    lines = readLines("11")
    xs = [ [ int(c) for c in line.strip() ] for line in lines ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()