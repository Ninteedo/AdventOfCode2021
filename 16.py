from typing import List, Tuple
from input_reader import readLines

class Packet:
    version: int
    typeId: int

    def __init__(self, version: int, typeId: int) -> None:
        self.version = version
        self.typeId = typeId

class LiteralPacket(Packet):
    value: int

    def __init__(self, version: int, typeId: int, value: int) -> None:
        super().__init__(version, typeId)
        self.value = value

class OperatorPacket(Packet):
    subPackets: List[Packet]

    def __init__(self, version: int, typeId: int, subPackets: List[Packet]) -> None:
        super().__init__(version, typeId)
        self.subPackets = subPackets

def part1(xs: str) -> int:
    return sumVersionNumbers(readPacket(hexToBin(xs))[0])

def part2(xs: str) -> int:
    return applyOperators(readPacket(hexToBin(xs))[0])

def sumVersionNumbers(packet: Packet) -> int:
    if packet.typeId == 4: # LiteralPacket
        return packet.version
    else: # OperatorPacket
        return packet.version + sum([ sumVersionNumbers(p) for p in packet.subPackets ])

def applyOperators(packet: Packet) -> int:
    if packet.typeId == 4: # LiteralPacket
        return packet.value
    else: # OperatorPacket
        subValues = [ applyOperators(p) for p in packet.subPackets ]
        if packet.typeId == 0: return sum(subValues)
        if packet.typeId == 1: return product(subValues)
        if packet.typeId == 2: return min(subValues)
        if packet.typeId == 3: return max(subValues)
        if packet.typeId == 5: return int(subValues[0] >  subValues[1])
        if packet.typeId == 6: return int(subValues[0] <  subValues[1])
        if packet.typeId == 7: return int(subValues[0] == subValues[1])

def product(nums: List[int]) -> int:
    result = 1
    for x in nums: result *= x
    return result

def readPacket(packetBin: List[int]) -> Tuple[Packet, int]:
    if binToDec(packetBin[3:6]) == 4: # LiteralPacket
        return readLiteralPacket(packetBin)
    else: # OperatorPacket
        return readOperatorPacket(packetBin)

def readLiteralPacket(packetBin: List[int]) -> Tuple[LiteralPacket, int]:
    continueBit = True
    totalBin = []
    offset = 0
    while continueBit:
        continueBit = packetBin[6+offset]
        totalBin += packetBin[7+offset:11+offset]
        offset += 5
    return (LiteralPacket(binToDec(packetBin[0:3]), binToDec(packetBin[3:6]), binToDec(totalBin)), 6+offset)

def readOperatorPacket(packetBin: List[int]) -> Tuple[OperatorPacket, int]:
    subPacketCount, subPacketsLength = 0, 0
    totalBinConsumed = 0
    if packetBin[6]: # check length type
        subPacketCount = binToDec(packetBin[7:18])
        totalBinConsumed += 18
    else:
        subPacketsLength = 22 + binToDec(packetBin[7:22])
        totalBinConsumed += 22
    remaining = packetBin[totalBinConsumed:]
    subPackets = []     # seperated from object field due to incorrect dereferencing
    while subPacketCount > 0 or subPacketsLength - totalBinConsumed > 0:
        newPacket, consumed = readPacket(remaining)
        subPackets.append(newPacket)
        remaining = remaining[consumed:]
        totalBinConsumed += consumed
        subPacketCount -= 1
    return (OperatorPacket(binToDec(packetBin[0:3]), binToDec(packetBin[3:6]), subPackets), totalBinConsumed)

def hexToBin(xs: str) -> List[int]:
    mappings = { "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111" }
    return [ int(x) for x in "".join([ mappings[c] for c in xs ]) ]

def binToDec(binary: List[int]) -> int:
    n = len(binary)
    return sum([ binary[i] * 2 ** (n-i-1) for i in range(n) ])

def main():
    lines = readLines("16")
    xs = lines[0].strip()

    print("Part 1", part1(xs))
    print("Part 2", part2(xs))

if __name__ == "__main__":
    main()