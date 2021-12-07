from typing import List, Tuple
from input_reader import readLines

def part1(xs: List[int]) -> int:
    xs.sort()
    median = xs[(len(xs)+1) // 2]
    return sum([ abs(x - median) for x in xs ])

def part2(xs: List[int]) -> int:
    mean = int(sum(xs) / len(xs))
    return min([ sum([ sum([ i+1 for i in range(abs(x - j)) ]) for x in xs ]) for j in range(mean-1, mean+1) ])

def main():
    xs = [ int(x) for x in readLines("07")[0].replace("\n", "").split(",") ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()