from typing import List
from input_reader import readLines

def part1(xs: List[List[int]]) -> int:
    '''Reasonable runtime <1s'''
    return a_star(xs)

def part2(xs) -> int:
    '''Terrible runtime ~20s'''
    return a_star(expandMap(xs))

def a_star(xs: List[List[int]]):
    # https://en.wikipedia.org/wiki/A*_search_algorithm

    open = set([ (0, 0) ])

    g = [ [ -1 for _ in range(len(xs[0])) ] for _ in range(len(xs)) ]
    g[0][0] = 0
    f = [ [ -1 for _ in range(len(xs[0])) ] for _ in range(len(xs)) ]
    f[0][0] = xs[0][0]

    while len(open) > 0:
        current = open.pop()    # can't get a random element from a set without popping it
        open.add(current)
        for o in open:
            if f[o[0]][o[1]] < f[current[0]][current[1]]: current = o
        if current == (len(xs)-1, len(xs[0])-1):
            return g[current[0]][current[1]]
        open.remove(current)

        for r, c in [ (1, 0), (0, 1), (-1, 0), (0, -1) ]:
            neighbour = (current[0]+r, current[1]+c)
            if validCoord(xs, neighbour[0], neighbour[1]):
                newG = g[current[0]][current[1]] + xs[neighbour[0]][neighbour[1]]
                if newG < g[neighbour[0]][neighbour[1]] or g[neighbour[0]][neighbour[1]] == -1:
                    g[neighbour[0]][neighbour[1]] = newG
                    f[neighbour[0]][neighbour[1]] = newG + (1 + r + c) * 2  # heuristic, positive when moving down or right, negative otherwise
                    if neighbour not in open: open.add(neighbour)
    return "failure"

def expandMap(xs: List[List[int]]) -> List[List[int]]:
    return [ [ (xs[r][c] + i + j - 1) % 9 + 1 for j in range(5) for c in range(len(xs)) ] for i in range(5) for r in range(len(xs)) ]

def validCoord(xs: List[List[int]], row: int, col: int) -> bool:
    return row >= 0 and row < len(xs) and col >= 0 and col < len(xs[0])

def main():
    lines = readLines("15")
    xs = [ [ int(c) for c in line.strip() ] for line in lines ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()