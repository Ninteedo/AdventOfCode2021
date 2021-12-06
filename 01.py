from typing import List
from input_reader import readLinesInt

def increaseCount(xs: List[int]) -> int:
    result = 0
    for i in range(1, len(xs)):
        if xs[i] > xs[i-1]:
            result += 1
    return result

def slidingIncreaseCount(xs: List[int]) -> int:
    result = 0
    for i in range(3, len(xs)):
        if (xs[i] + xs[i-1] + xs[i-2]) > (xs[i-1] + xs[i-2] + xs[i-3]):
            result += 1
    return result

def main():
    xs = readLinesInt("01")

    print("Part 1", increaseCount(xs))
    print("Part 2", slidingIncreaseCount(xs))

if __name__ == "__main__":
    main()