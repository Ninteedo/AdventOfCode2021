from input_reader import readLines
from re import match, compile

def part1(yMin: int) -> int:
    return (yMin * (yMin+1)) // 2

def part2(xMin: int, xMax: int, yMin: int, yMax: int) -> int:
    return sum([ sum([ hitsTarget(xVel, yVel, xMin, xMax, yMin, yMax) for xVel in range(xMax+1) ]) for yVel in range(yMin, -yMin) ])

def hitsTarget(xVel: int, yVel: int, xMin: int, xMax: int, yMin: int, yMax: int) -> bool:
    for steps in range(round(stepsToY(yMax, yVel)), round(stepsToY(yMin, yVel))+1):
        x = ((xVel * (xVel+1)) // 2) - (max(xVel-steps, 0) * ((max(xVel-steps, 0)+1)) // 2)
        y = (steps * yVel) - ((steps * (steps-1)) // 2)
        if x >= xMin and x <= xMax and y >= yMin and y <= yMax:
            return True
    return False

def stepsToY(y, yVel):
    return ((4*(yVel**2) + 4*yVel - 8*y + 1) ** 0.5 + 2*yVel + 1) / 2

def main():
    lines = readLines("17")
    pattern = compile("^target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)..(-?\d+)$")
    matches = match(pattern, lines[0].strip())
    xMin, xMax, yMin, yMax = matches.groups()

    print("Part 1", part1(int(yMin)))
    print("Part 2", part2(int(xMin), int(xMax), int(yMin), int(yMax)))

if __name__ == "__main__":
    main()