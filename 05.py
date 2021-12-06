from typing import List, Tuple
from input_reader import readLines

class Line:

    def __init__(self, coords: List[str]) -> None:
        self.x1 = int(coords[0])
        self.y1 = int(coords[1])
        self.x2 = int(coords[2])
        self.y2 = int(coords[3])

class OverlapDiagram:

    def __init__(self, lines: List[Line]) -> None:
        xVals = [ x.x1 for x in lines ] + [ x.x2 for x in lines ]
        yVals = [ x.y1 for x in lines ] + [ x.y2 for x in lines ]
        self.minX, self.maxX = min(xVals), max(xVals)
        self.minY, self.maxY = min(yVals), max(yVals)

        self.overlapBoard = [ [ 0 for _ in range(self.minY, self.maxY+1) ] for _ in range(self.minX, self.maxX+1) ]

    def incrementOverlapCount(self, x: int, y: int) -> None:
        self.overlapBoard[x - self.minX][y - self.minY] += 1

    def getOverlapCount(self, x: int, y: int) -> int:
        return self.overlapBoard[x - self.minX][y - self.minY]

def countOverlaps(diagram: OverlapDiagram) -> int:
    return sum([ sum([ diagram.getOverlapCount(x, y) > 1 for y in range(diagram.minY, diagram.maxY+1) ]) for x in range(diagram.minX, diagram.maxX+1)])

def part1(xs: List[Line]) -> int:
    lines = [ x for x in xs if x.x1 == x.x2 or x.y1 == x.y2]
    diagram = OverlapDiagram(lines)
    for line in lines:
        yAligned = line.y1 == line.y2
        if yAligned:    static, l, r = line.y1, line.x1, line.x2
        else:           static, l, r = line.x1, line.y1, line.y2
        for dynamic in range(min(l, r), max(l, r)+1):
            if yAligned:    x, y = dynamic, static
            else:           x, y = static, dynamic
            diagram.incrementOverlapCount(x, y)
    return countOverlaps(diagram)

def part2(xs: List[Line]) -> int:
    lines = [ x for x in xs if x.x1 == x.x2 or x.y1 == x.y2 or abs(x.x1 - x.x2) == abs(x.y1 - x.y2) ]
    diagram = OverlapDiagram(lines)
    for line in lines:
        xDiff, yDiff = line.x1 - line.x2, line.y1 - line.y2
        if xDiff == 0:
            x = line.x1
            for y in range(min(line.y1, line.y2), max(line.y1, line.y2)+1):
                diagram.incrementOverlapCount(x, y)
        else:
            gradient = yDiff // xDiff
            if line.x1 <= line.x2:  xStart, yStart = line.x1, line.y1
            else:                   xStart, yStart = line.x2, line.y2
            for x in range(xStart, max(line.x1, line.x2)+1):
                y = gradient * (x-xStart) + yStart
                diagram.incrementOverlapCount(x, y)
    return countOverlaps(diagram)

def main():
    lines = readLines("05")

    xs = [ Line(line.replace(" -> ", ",").split(",")) for line in lines ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()