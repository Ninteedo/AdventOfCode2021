from typing import List, Tuple, Dict
from input_reader import readLines

def part1(template: str, rules: List[Tuple[str, str]]) -> int:
    return runPolymerisation(template, rules, 10)

def part2(template: str, rules: List[Tuple[str, str]]) -> int:
    return runPolymerisation(template, rules, 40)

def runPolymerisation(template: str, rules: List[Tuple[str, str]], steps: int):
    empty = {}
    for rule in rules: empty[rule] = 0
    current = empty.copy()
    for i in range(len(template)-1):
        l, r = template[i], template[i+1]
        current[l+r] += 1
    for _ in range(steps):
        new = empty.copy()
        for rule in current:
            new[rule[0]+rules[rule]] += current[rule]
            new[rules[rule]+rule[1]] += current[rule]
        current = new
    return findMaxMinElementDifference(template, current)

def findMaxMinElementDifference(template: str, compound: Dict[str, int]) -> int:
    sums = {}
    for rule in compound:
        l, r = rule[0], rule[1]
        if l not in sums: sums[l] = 0
        if r not in sums: sums[r] = 0
        sums[l] += compound[rule]
        sums[r] += compound[rule]
    sums[template[0]]  += 1
    sums[template[-1]] += 1
    min, max = 0, 0
    for element in sums:
        if sums[element] < min or min == 0:  min = sums[element]
        if sums[element] > max:              max = sums[element]
    return (max - min) // 2

def main():
    lines = readLines("14")
    template = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        rules[line[0:2]] = line.strip()[-1]

    print("Part 1", part1(template, rules))
    print("Part 2", part2(template, rules))

if __name__ == "__main__":
    main()