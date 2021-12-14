from typing import List
from input_reader import readLines

def part1(xs: List[str]) -> int:
    '''O(mn)'''
    scores = { None: 0, ")": 3, "]": 57, "}": 1197, ">": 25137 }
    return sum([ scores[corruptedBracket(line)] for line in xs ])

def part2(xs: List[str]) -> int:
    '''O(mn)'''
    totals = [ lineScore(line) for line in xs if corruptedBracket(line) == None ]
    totals.sort()
    return totals[len(totals)//2]

def corruptedBracket(line: str) -> str:
    '''O(n)'''
    pairs = { "(": ")", "[": "]", "{": "}", "<": ">" }
    opened = []
    for c in line:
        if c in pairs:
            opened.append(c)
        else:
            requiredBracket = pairs[opened.pop()]
            if c != requiredBracket:
                return c
    return None

def lineScore(line: str) -> int:
    '''O(n)'''
    scores = { ")": 1, "]": 2, "}": 3, ">": 4 }
    pairs = { "(": ")", "[": "]", "{": "}", "<": ">" }
    opened = []
    for c in line:
        if c in pairs:  opened.append(c)
        else:           opened.pop()
    return sum([ scores[pairs[c]] * (5 ** i) for i, c in enumerate(opened) ])

def main():
    lines = readLines("10")
    xs = [ line.strip() for line in lines ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()