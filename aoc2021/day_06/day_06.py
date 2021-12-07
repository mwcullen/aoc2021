from typing import List, NamedTuple, Tuple
from enum import Enum
from dataclasses import dataclass


def advanceDay(l1: List[int]) -> List[int]:
    newFishPerDay: List[int] = [0]*9
    for i in range(9):
        if i == 0:
            newFishPerDay[8] = l1[i]
            newFishPerDay[6] += l1[i]
        else:
            newFishPerDay[i-1] += l1[i]

    return newFishPerDay


def main():
    f = open("./input1.txt", "r", encoding='utf8')

    rawString = f.read()

    lstStartingFish = rawString.split(',')

    lstFishPerDay: List[int] = [0]*9

    for fish in lstStartingFish:
        lstFishPerDay[int(fish)] += 1

    for _ in range(256):
        lstFishPerDay = advanceDay(lstFishPerDay)

    sumFish:int = 0
    for fish in lstFishPerDay:
        sumFish += fish

    print(sumFish)






if __name__ == '__main__':
    main()
