from typing import List

def readLines(fileName: str) -> List[str]:
    f = open(f"input/{fileName}.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def readLinesInt(fileName: str) -> List[int]:
    lines = readLines(fileName)
    xs = []
    for line in lines:
        xs.append(int(line))
    return xs