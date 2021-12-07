from typing import List
from input_reader import readLinesInt

def part1(xs: List[int]) -> int:
    '''O(n)'''
    return sum([ xs[i] > xs[i-1] for i in range(1, len(xs)) ])

def part2(xs: List[int]) -> int:
    '''O(n)'''
    return sum([ xs[i] > xs[i-3] for i in range(3, len(xs)) ])

def main():
    xs = readLinesInt("01")

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()