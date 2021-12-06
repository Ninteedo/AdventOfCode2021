from typing import List
from input_reader import readLines

def countLanternFish(startingFish: List[int], days: int) -> int:
    resetDayCount, initialDayCount = 6, 8
    daysRemaining = days
    fishTimers = [ sum([ x == i for x in startingFish ]) for i in range(0, initialDayCount+1) ]
    for _ in range(0, daysRemaining):
        fishTimers = [ fishTimers[i+1] if i != resetDayCount else fishTimers[i+1] + fishTimers[0] for i in range(0, initialDayCount) ] + [ fishTimers[0] ]
    return sum(fishTimers)

def part1(xs: List[int]) -> int:
    return countLanternFish(xs, 80)

def part2(xs: List[int]) -> int:
    return countLanternFish(xs, 256)

def main():
    xs = [ int(x) for x in readLines("06")[0].replace("\n", "").split(",") ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()