from typing import List
from input_reader import readLines

def part1(xs: List[int]) -> int:
    '''Sort method is O(n log n), otherwise O(n)'''
    xs.sort()
    median = xs[(len(xs)+1) // 2]
    return sum([ abs(x - median) for x in xs ])

def part2(xs: List[int]) -> int:
    '''O(n), but runtime scales with variance of inputs'''
    mean = int(sum(xs) / len(xs))
    return min([ sum([ (abs(x - j) * (abs(x - j) + 1)) // 2 for x in xs ]) for j in range(mean-1, mean+1) ])

def main():
    xs = [ int(x) for x in readLines("07")[0].replace("\n", "").split(",") ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()