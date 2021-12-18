from typing import List, Tuple
from input_reader import readLines
from functools import reduce
from copy import deepcopy

class SnailNum:
    isValue: bool
    value: int
    left: "SnailNum"
    right: "SnailNum"
    parent: "SnailNum"
    
    def __init__(self) -> None:
        self.parent = None

    def __str__(self) -> str:
        if self.isValue:
            return str(self.value)
        else:
            return f"[{str(self.left)},{str(self.right)}]"

    def __repr__(self) -> str:
        return str(self)

def part1(xs: List[SnailNum]) -> int:
    return getMagnitude(reduce(addSnailNums, xs[1:], xs[0]))

def part2(xs: List[SnailNum]) -> int:
    '''Slow ~5s'''
    mags = [ getMagnitude(addSnailNums(deepcopy(x), deepcopy(y))) for x in xs for y in xs if x is not y ]
    # print(mags)
    return max(mags)

def addSnailNums(left: SnailNum, right: SnailNum) -> SnailNum:
    result = SnailNum()
    result.isValue = False
    result.left, result.right = left, right
    result.left.parent, result.right.parent = result, result
    while True:
        explosion = findReduction(result, False)
        if explosion != None: doExplosion(explosion)
        else:
            split = findReduction(result, True)
            if split != None: doSplit(split)
            else: break
    return result

def findReduction(num: SnailNum, mode: bool, depth: int=0) -> Tuple[bool, SnailNum]:
    if not mode and not num.isValue and depth >= 4: return num  # check for explosion
    elif mode and num.isValue and num.value > 9:    return num  # check for split
    elif not num.isValue:
        l = findReduction(num.left, mode, depth+1)
        if l != None: return l
        else:         return findReduction(num.right, mode, depth+1)
    return None

def doExplosion(start: SnailNum) -> None:
    start.value = 0
    start.isValue = True
    l, r = start.left.value, start.right.value
    curr, prev = start, start
    while curr != None:
        prev = curr
        curr = curr.parent
        if curr == None:
            break
        if prev is not curr.left:
            curr = curr.left
            while not curr.isValue:
                curr = curr.right
            curr.value += l
            break
    curr, prev = start, start
    while curr != None:
        prev = curr
        curr = curr.parent
        if curr == None:
            break
        if prev is not curr.right:
            curr = curr.right
            while not curr.isValue:
                curr = curr.left
            curr.value += r
            break
        
def doSplit(curr: SnailNum) -> None:
    curr.isValue = False
    curr.left, curr.right = SnailNum(), SnailNum()
    curr.left.parent, curr.right.parent = curr, curr
    curr.left.isValue, curr.right.isValue = True, True
    curr.left.value = curr.value // 2
    curr.right.value = curr.value - curr.left.value

def getMagnitude(curr: SnailNum) -> int:
    if curr.isValue: return curr.value
    else: return 3 * getMagnitude(curr.left) + 2 * getMagnitude(curr.right)

def readSnailNum(input: str) -> SnailNum:
    depth = 0
    result = SnailNum()
    if input[0] != "[":
        result.isValue = True
        result.value = int(input)
    else:
        for i, c in enumerate(input):
            if   c == "[": depth += 1
            elif c == "]": depth -= 1
            elif depth == 1 and c == ",":
                result.isValue = False
                result.left = readSnailNum(input[1:i])
                result.right = readSnailNum(input[i+1:-1])
                result.left.parent, result.right.parent = result, result
                break
    return result

def main():
    lines = readLines("18")
    xs = [ readSnailNum(line.strip()) for line in lines ]

    print("Part 1", part1(deepcopy(xs)))
    print("Part 2", part2(deepcopy(xs)))

if __name__ == "__main__":
    main()