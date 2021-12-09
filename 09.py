from typing import List, Tuple
from input_reader import readLines, readLinesInt

MAXVALUE = None

def part1(xs: List[List[int]]) -> int:
    '''O(mn)'''
    adjancents = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    lowPointsMask = [ [ all([ checkLower(xs, rowNum, colNum, rowNum+r, colNum+c) for r, c in adjancents ]) for colNum in range(len(xs[0])) ] for rowNum in range(len(xs)) ]
    return sum([ xs[row][col]+1 for row in range(len(xs)) for col in range(len(xs[0])) if lowPointsMask[row][col] ])

def checkLower(xs: List[List[int]], row: int, col: int, otherRow: int, otherCol: int) -> bool:
    '''O(1)'''
    return not validCoord(xs, otherRow, otherCol) or xs[row][col] < xs[otherRow][otherCol]

def validCoord(xs: List[List[int]], row: int, col: int) -> bool:
    '''O(1)'''
    return row >= 0 and row < len(xs) and col >= 0 and col < len(xs[0])

def part2(xs: List[List[int]]) -> int:
    '''O(mn)'''
    basinCount = 0
    basinMap = [ [ 0 for _ in range(len(xs[0])) ] for _ in range(len(xs)) ]
    for rowNum in range(len(xs)):
        for colNum in range(len(xs[0])):
            updateCoords = [ (rowNum, colNum) ]
            i = 0
            while i < len(updateCoords):
                r, c = updateCoords[i]
                updated, basinCount = updateBasin(xs, basinMap, r, c, basinCount)
                if updated:
                    updateCoords += [ (r-1, c), (r, c-1) ]
                i += 1
    basinSizes = [ len([ i for row in range(len(xs)) for col in range(len(xs[0])) if basinMap[row][col] == i ]) for i in range(1, basinCount) ]
    basinSizes.sort(reverse=True)
    return basinSizes[0] * basinSizes[1] * basinSizes[2]

def printBasinMap(basinMap: List[List[int]]):
    result = "\n".join([ "".join([ str(basinMap[row][col]) if basinMap[row][col] != None else "." for col in range(len(basinMap[0])) ]) for row in range(len(basinMap)) ])
    print(result)

def updateBasin(xs: List[List[int]], basinMap: List[List[int]], rowNum: int, colNum: int, basinCount: int) -> Tuple[bool, int]:
    '''O(1)'''
    if validCoord(xs, rowNum, colNum):
        if xs[rowNum][colNum] == 9:
            basinMap[rowNum][colNum] = MAXVALUE
        else:
            neighbour = checkForBasinNeighbours(basinMap, rowNum, colNum)
            if neighbour == 0:
                basinCount += 1
                basinMap[rowNum][colNum] = basinCount
                return True, basinCount
            elif neighbour != basinMap[rowNum][colNum]:
                basinMap[rowNum][colNum] = neighbour
                return True, basinCount
    return False, basinCount

def checkForBasinNeighbours(basinMap: List[List[int]], row: int, col: int) -> int:
    '''O(1)'''
    neighbours = [ basinMap[row+r][col+c] for r, c in [ (0, 0), (-1, 0), (1, 0), (0, -1), (0, 1) ] if validCoord(basinMap, row+r, col+c) ]
    neighbours = [ x for x in neighbours if x != 0 and x != MAXVALUE ]
    if len(neighbours) == 0:
        return 0
    else:
        return min(neighbours)

def main():
    lines = readLines("09")
    xs = [ [ int(char) for char in line.replace("\n", "") ] for line in lines ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()