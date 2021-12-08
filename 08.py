from typing import List, Tuple
from input_reader import readLines

SegInstr = Tuple[List[str], List[str]]

def part1(xs: List[SegInstr]) -> int:
    '''O(n)'''
    uniqueLengths = [ 2, 3, 4, 7 ]
    return sum([ len(digit) in uniqueLengths for _, outputs in xs for digit in outputs ] )

def part2(xs: List[SegInstr]) -> int:
    '''O(n) * O(1) == O(n)'''
    total = 0
    for inputs, outputs in xs:
        segmentRules = determineSegmentRules(inputs)
        total += int("".join([ str(i) for digit in outputs for i in range(10) if len(segmentDifference(digit, segmentRules[i])) == 0 ]))
    return total

def determineSegmentRules(inputs: List[str]) -> List[str]:
    '''O(1)'''
    uniqueSegmentMappings = [ (1, 2), (7, 3), (4, 4), (8, 7) ]  # each pair is digit, segment count
    segmentRules = [""] * 10
    ambiguousFiveSeg = []
    ambiguousSixSeg = []
    for digit in inputs:
        m = len(digit)
        if m == 5:
            ambiguousFiveSeg.append(digit)
        elif m == 6:
            ambiguousSixSeg.append(digit)
        else:
            for i, j in uniqueSegmentMappings:
                if j == m:
                    segmentRules[i] = digit
                    break
    for digit in ambiguousFiveSeg:
        if len(segmentDifference(segmentRules[1], digit)) == 3:
            segmentRules[3] = digit
        elif len(segmentDifference(segmentRules[4], digit)) == 3:
            segmentRules[5] = digit
        else:
            segmentRules[2] = digit
    for digit in ambiguousSixSeg:
        if len(segmentDifference(segmentRules[5], digit)) == 3:
            segmentRules[0] = digit
        elif len(segmentDifference(segmentRules[7], digit)) == 3:
            segmentRules[9] = digit
        else:
            segmentRules[6] = digit
    return segmentRules

def segmentDifference(a: str, b: str) -> str:
    '''O(1)'''
    return [ charA for charA in a if charA not in b ] + [ charB for charB in b if charB not in a ]

def main():
    lines = readLines("08")
    lines = [ line.replace("\n", "").replace(" | ", "|") for line in lines]
    xs = [ (line.split("|")[0].split(" "), line.split("|")[1].split(" ")) for line in lines if line != "" ]

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()