from typing import List, Tuple
from input_reader import readLines

from heapq import heappush, heappop

def part1(xs: List[List[int]]) -> int:
    return a_star(xs)

def part2(xs) -> int:
    '''Bad runtime ~4s'''
    return a_star(expandMap(xs))

def a_star(xs: List[List[int]]):
    # https://en.wikipedia.org/wiki/A*_search_algorithm

    open = [ (-1, (0, 0)) ]
    g = [ [ -1 for _ in range(len(xs[0])) ] for _ in range(len(xs)) ]
    g[0][0] = 0
    target = (len(xs)-1, len(xs[0])-1)
    while len(open) > 0:
        current = heappop(open)[1]
        if current == target:
            return gridGet(g, current)
        for r, c in [ (1, 0), (0, 1), (-1, 0), (0, -1) ]:
            adj = (current[0]+r, current[1]+c)
            if validCoord(xs, adj):
                oldG, newG = gridGet(g, adj), gridGet(g, current) + gridGet(xs, adj)
                if newG < oldG or oldG == -1:
                    g[adj[0]][adj[1]] = newG
                    h = r + c  # heuristic, positive when moving towards target, negative otherwise
                    if adj not in open: heappush(open, (newG + h, adj))
    return "failure"

def expandMap(xs: List[List[int]]) -> List[List[int]]:
    return [ [ (xs[r][c] + i + j - 1) % 9 + 1 for j in range(5) for c in range(len(xs)) ] for i in range(5) for r in range(len(xs)) ]

def validCoord(xs: List[List[int]], coord: Tuple[int, int]) -> bool:
    return coord[0] >= 0 and coord[0] < len(xs) and coord[1] >= 0 and coord[1] < len(xs[0])

def gridGet(xs: List[List[int]], coord: Tuple[int, int]) -> int:
    return xs[coord[0]][coord[1]]

def main():
    lines = readLines("15")
    xs = [ [ int(c) for c in line.strip() ] for line in lines ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()