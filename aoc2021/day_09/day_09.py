from typing import List
from dataclasses import dataclass
from typing import Dict
from typing import NamedTuple


@dataclass
class HeightMap:
    grid: List[List[int]]
    maxX: int
    maxY: int

    def returnVal(self, x: int, y: int) -> int:
        if x >= 0 and x < self.maxX and y >= 0 and y < self.maxY:
            return self.grid[y][x]
        else:
            return None

    def checkForLowPoint(self, x: int, y: int) -> bool:
        lowPoint = True
        aboveCoords = self.returnVal(x, y-1)
        belowCoords = self.returnVal(x, y+1)
        leftCoords = self.returnVal(x-1, y)
        rightCoords = self.returnVal(x+1, y)
        currentVal = self.returnVal(x, y)

        if aboveCoords is not None and aboveCoords <= currentVal:
            lowPoint = False
        elif belowCoords is not None and belowCoords <= currentVal:
            lowPoint = False
        elif leftCoords is not None and leftCoords <= currentVal:
            lowPoint = False
        elif rightCoords is not None and rightCoords <= currentVal:
            lowPoint = False
        
        return lowPoint


def main():
    f = open("./inputTest.txt", "r", encoding='utf8')

    rawString = f.read()

    lines = rawString.splitlines()

    lstPoints: List[List[int]] = []

    for line in lines:

        tempList: List[int] = [int(x) for x in list(line)]

        lstPoints.append(tempList)

    heightMap = HeightMap(grid=lstPoints, maxX=len(
        lstPoints[0]), maxY=len(lstPoints))

    totalLowPoints: int = 0
    for i, yList in enumerate(heightMap.grid):
        for j, xVals in enumerate(yList):
            if heightMap.checkForLowPoint(j, i):
                totalLowPoints += heightMap.grid[i][j] + 1
                print(heightMap.grid[i][j])
    print(totalLowPoints)


if __name__ == '__main__':
    main()
