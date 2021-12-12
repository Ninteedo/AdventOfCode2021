from typing import List, Dict
from input_reader import readLines

startStr = "start"
endStr = "end"

def part1(xs: Dict[str, List[str]]) -> int:
    return len(getPaths([startStr], xs, True))

def part2(xs: Dict[str, List[str]]) -> int:
    return len(getPaths([startStr], xs, False))

def getPaths(currentPath: List[str], connections: Dict[str, List[str]], revisited: bool) -> List[List[str]]:
    '''O((vertex count)!)'''
    current = currentPath[-1]
    paths = []
    if current == endStr:
        paths = [currentPath]
    elif current in connections:
        for connection in connections[current]:
            baseCond = connection.isupper() or connection not in currentPath
            if baseCond or (not revisited and connection != startStr and connection != endStr):
                paths += [ path for path in getPaths(currentPath + [connection], connections, revisited or not baseCond) ]
    return paths

def main():
    lines = readLines("12")
    xs = {}
    for line in lines:
        v1, v2 = line.strip().split("-")
        for a, b in [(v1, v2), (v2, v1)]:
            if a not in xs:
                xs[a] = [b]
            if b not in xs[a]:
                xs[a].append(b)

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()