from typing import List, Tuple
from functools import reduce
from input_reader import readLines

def part1(dots: List[Tuple[int, int]], folds: List[Tuple[str, int]]) -> int:
    state = doFold(dots, folds[0])
    uniques = set(state)
    return len(uniques)

def part2(dots: List[Tuple[int, int]], folds: List[Tuple[str, int]]) -> int:
    state = reduce(doFold, folds, dots)
    printBoard(state)
    return "read 8 capital letters from printed board"

def doFold(dots: List[Tuple[int, int]], fold: Tuple[str, int]) -> List[Tuple[int, int]]:
    state = dots
    xFold = fold[0] == "x"
    for i, dot in enumerate(state):
        if xFold:   state[i] = (fold[1] - abs(dot[0] - fold[1]), dot[1])
        else:       state[i] = (dot[0], fold[1] - abs(dot[1] - fold[1]))
    return state

def printBoard(dots: List[Tuple[int, int]]) -> None:
    maxX, maxY = max([ dot[0] for dot in dots ]), max([ dot[1] for dot in dots ])
    board = [ [ " " for _ in range(maxX+1) ] for _ in range(maxY+1) ]
    for dot in dots: board[dot[1]][dot[0]] = "#"
    print("\n".join([ "".join(row) for row in board ]))

def main():
    lines = readLines("13")
    dots = [ (int(lines[i].split(",")[0]), int(lines[i].strip().split(",")[1])) for i in range(lines.index("\n")) ]
    folds = [ (lines[i].split("=")[0][-1], int(lines[i].strip().split("=")[1])) for i in range(lines.index("\n")+1, len(lines)) ]

    print("Part 1", part1(dots, folds))
    print("Part 2", part2(dots, folds))

if __name__ == "__main__":
    main()