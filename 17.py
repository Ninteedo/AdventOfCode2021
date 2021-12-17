from input_reader import readLines
from re import match, compile

def part1(yMin: int) -> int:
    return (yMin * (yMin+1)) // 2

def part2(xMin: int, xMax: int, yMin: int, yMax: int) -> int:
    return sum([ sum([ hitsTarget(xVel, yVel, xMin, xMax, yMin, yMax) for xVel in range(0, xMax+1) ]) for yVel in range(yMin, abs(yMin)) ])

def hitsTarget(xVel: int, yVel: int, xMin: int, xMax: int, yMin: int, yMax: int) -> bool:
    x, y, steps = 0, 0, 0
    while y >= yMin and x <= xMax:
        x += max(xVel - steps, 0)
        y += yVel - steps
        steps += 1
        if x >= xMin and x <= xMax and y >= yMin and y <= yMax:
            return True
    return False

def main():
    lines = readLines("17")
    pattern = compile("^target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)..(-?\d+)$")
    matches = match(pattern, lines[0].strip())
    xMin, xMax, yMin, yMax = matches.groups()

    print("Part 1", part1(int(yMin)))
    print("Part 2", part2(int(xMin), int(xMax), int(yMin), int(yMax)))

if __name__ == "__main__":
    main()