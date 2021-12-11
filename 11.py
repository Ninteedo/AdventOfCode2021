from typing import List
from input_reader import readLines

def part1(xs: List[List[int]]) -> int:
    '''O(steps * nm)'''
    steps = 100
    states = xs
    flashes = 0
    for step in range(steps):
        states = processStep(states)
        flashes += countFlashes(states)
    return flashes

def part2(xs: List[List[int]]) -> int:
    '''O(steps * nm)'''
    flashes, target = 0, len(xs) * len(xs[0])
    step = 0
    states = xs
    while flashes != target:
        step += 1
        states = processStep(states)
        flashes = countFlashes(states)
    return step

def processStep(xs: List[List[int]]) -> List[List[int]]:
    '''O(nm)'''
    n, m = len(xs), len(xs[0])
    states = [ [ xs[row][col] + 1 for col in range(len(xs[0])) ] for row in range(len(xs)) ]
    flashes = [ (row, col) for col in range(len(xs[0])) for row in range(len(xs)) if states[row][col] > 9 ]
    while flashes != []:
        row, col = flashes.pop()
        if states[row][col] > 9:
            states[row][col] = 0
            adjacencies = [ (r, c) for r in [-1, 0, 1] for c in [-1, 0, 1] if (r != 0 or c != 0) and validCoord(row+r, col+c, n, m) and states[row+r][col+c] != 0 ]
            for r, c in adjacencies:
                states[row+r][col+c] += 1
                flashes.append((row+r, col+c))
    return states

def validCoord(row: int, col: int, rows: int, cols: int) -> bool:
    '''O(1)'''
    return row >= 0 and row < rows and col >= 0 and col < cols

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