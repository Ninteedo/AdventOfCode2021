from typing import List
from input_reader import readLines

Board = List[List[int]]
BoardMarks = List[List[bool]]

boardSize = 5

def createBoardMarks(boardCount: int) -> List[BoardMarks]:
    return [ [ [ False for _ in range(0, boardSize)] for _ in range(0, boardSize)] for _ in range(0, boardCount) ]

def applyBingoDraw(draw: int, boards: List[Board], boardMarks: List[BoardMarks]) -> List[BoardMarks]:
    return [ [ [ boardMarks[i][k][j] or boards[i][k][j] == draw for j in range(0, boardSize) ] for k in range(0, boardSize) ] for i in range(0, len(boards)) ]

def testBingo(boardMarks: BoardMarks) -> bool:
    return any([ sum(boardMarks[rowNum]) == boardSize for rowNum in range(0, boardSize) ] + [ sum([ boardMarks[i][colNum] for i in range(0, boardSize) ]) == boardSize for colNum in range(0, boardSize) ])

def calculateUnmarkedSum(board: Board, markBoard: BoardMarks) -> int:
    return sum([ board[j][k] for j in range(0, boardSize) for k in range(0, boardSize) if not markBoard[j][k] ])

def part1(draws: List[int], boards: List[Board]) -> int:
    boardMarks = createBoardMarks(len(boards))
    for draw in draws:
        boardMarks = applyBingoDraw(draw, boards, boardMarks)
        for i in range(0, len(boards)):
            if testBingo(boardMarks[i]):
                return draw * calculateUnmarkedSum(boards[i], boardMarks[i])

def part2(draws: List[int], boards: List[Board]) -> int:
    boardMarks = createBoardMarks(len(boards))
    remainingBoards = [True] * len(boards)
    for draw in draws:
        boardMarks = applyBingoDraw(draw, boards, boardMarks)
        for i in range(0, len(boards)):
            if remainingBoards[i] and testBingo(boardMarks[i]):
                remainingBoards[i] = False
                if sum(remainingBoards) == 0:
                    return draw * calculateUnmarkedSum(boards[i], boardMarks[i])

def main():
    lines = readLines(4)

    draws = [ int(x.replace("\n", "")) for x in lines[0].split(",") if x != "" ]
    boards = [ [ [ int(x.replace("\n", "")) for x in lines[i+j].split(" ") if x != "" ] for j in range(0, boardSize) ] for i in range(2, len(lines), boardSize+1) ]

    print("Part 1", part1(draws, boards))
    print("Part 2", part2(draws, boards))

if __name__ == "__main__":
    main()