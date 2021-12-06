from typing import List
from input_reader import readLines

def part1(xs: List[List[int]]) -> int:
    n = len(xs)
    bitCount = len(xs[0])
    digitSums = [ sum([ x[bitCount - i - 1] for x in xs ]) for i in range(0, bitCount) ]
    gamma = sum([ 2 ** i for i in range(0, bitCount) if digitSums[i] >= n/2 ])
    return gamma * (2 ** bitCount - gamma - 1)

def part2(xs: List[List[int]]) -> int:
    return filterByBitCriteria(xs, True) * filterByBitCriteria(xs, False)

def filterByBitCriteria(xs: List[List[int]], toggleFilterValue: bool) -> int:
    n = len(xs)
    bitCount = len(xs[0])
    ratingsValid = [True] * n
    for i in range(0, bitCount):
        bitSum = sum([ xs[j][i] for j in range(0, n) if ratingsValid[j] ])
        filterValue = abs(toggleFilterValue - (bitSum >= sum(ratingsValid)/2))
        if sum(ratingsValid) == 1:
            break
        ratingsValid = [ ratingsValid[j] and xs[j][i] == filterValue for j in range(0, n) ]
    
    return sum([ xs[j][bitCount - i - 1] * (2 ** i) for j in range(0, n) for i in range(0, bitCount) if ratingsValid[j] ])

def main():
    lines = readLines("03")
    xs = []
    for line in lines:
        x = []
        for c in line:
            if c != "\n":
                x.append(int(c))
        xs.append(x)

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()