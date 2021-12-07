from typing import List
from math import ceil


def sumFuel(num: int) -> int:
    finalSum = 0
    for i in range(num+1):
        finalSum += i

    return finalSum


def main():
    f = open("./input1.txt", "r", encoding='utf8')

    rawString = f.read()

    lstNumsStr: List[str] = rawString.split(',')
    lstNums: List[int] = list(map(int, lstNumsStr))

    lstNums.sort()

    medianIndex: int = ceil(len(lstNums)/2)
    medianValue: int = lstNums[medianIndex]

    totalFuel: int = 0
    sumforaverage: int = 0
    for num in lstNums:
        totalFuel += abs(num - medianValue)
        sumforaverage += num

    print(totalFuel)

    averageVal: int = ceil(sumforaverage/len(lstNums))

    secondaryTotalFuel: int = 0
    secondaryTotalFuelPlus1: int = 0
    for num in lstNums:
        secondaryTotalFuel += sumFuel(abs(num-averageVal))

        secondaryTotalFuelPlus1 += sumFuel(abs(num-averageVal+1))

    print(secondaryTotalFuel, secondaryTotalFuelPlus1)


if __name__ == '__main__':
    main()
