from typing import List
from input_reader import readLines

def part1(xs: List[List[int]]) -> int:
    n = len(xs)
    bitCount = len(xs[0])
    digitSums = [0] * bitCount
    for x in xs:
        for i, bit in enumerate(x):
            digitSums[bitCount - i - 1] += bit
    
    gamma = 0
    for i in range(0, bitCount):
        if digitSums[i] >= n/2:
            gamma += 2 ** i

    return gamma * (2 ** (bitCount) - gamma - 1)

def part2(xs: List[List[int]]) -> int:
    return filterByBitCriteria(xs, True) * filterByBitCriteria(xs, False)

def filterByBitCriteria(xs: List[List[int]], toggleFilterValue: bool) -> int:
    n = len(xs)
    bitCount = len(xs[0])
    ratingsValid = [True] * n

    for i in range(0, bitCount):
        bitSum = 0
        for j in range(0, n):
            if ratingsValid[j]:
                bitSum += xs[j][i]

        remainingValues = sum(ratingsValid)
        filterValue = 0
        if bitSum >= remainingValues/2:
            filterValue = 1
        if toggleFilterValue:
            filterValue = 1 - filterValue
        
        for j in range(0, n):
            if remainingValues > 1:
                if ratingsValid[j] and xs[j][i] != filterValue:
                    ratingsValid[j] = False
    
    decValue = 0
    for j in range(0, n):
        if ratingsValid[j]:
            if decValue > 0:
                raise ValueError
            for i in range(0, bitCount):
                decValue += xs[j][bitCount - i - 1] * 2 ** i

    return decValue

def main():
    lines = readLines(3)
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