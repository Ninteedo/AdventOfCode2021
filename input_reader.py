from typing import List

def readLines(challengeNumber: int) -> List[str]:
    f = open(f"input/{challengeNumber}.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def readLinesInt(challengeNumber: int) -> List[int]:
    lines = readLines(challengeNumber)
    xs = []
    for line in lines:
        xs.append(int(line))
    return xs