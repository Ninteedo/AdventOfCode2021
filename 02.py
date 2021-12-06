from typing import List, Tuple
from input_reader import readLines

Command = Tuple[str, int]

def part1(xs: List[Command]) -> int:
    x = 0
    y = 0
    for command, value in xs:
        if command == "forward":
            x += value
        elif command == "down":
            y += value
        else:
            y -= value
    return x * y

def part2(xs: List[Command]) -> int:
    x = 0
    y = 0
    aim = 0
    for command, value in xs:
        if command == "forward":
            x += value
            y += aim * value
        elif command == "down":
            aim += value
        else:
            aim -= value
    return x * y

def readCommands() -> List[Command]:
    lines = readLines("02")
    result = []
    for line in lines:
        splits = line.split(" ")
        result.append((splits[0], int(splits[1])))
    return result

def main():
    xs = readCommands()

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()