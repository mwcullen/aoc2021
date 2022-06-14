from typing import List
from dataclasses import dataclass


@dataclass
class HeightMap:
    grid: List[List[int]]
    maxX: int
    maxY: int

    class outOfBoundsException(Exception):
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y
            self.message = f"out of bounds at x={x} y={y}"

    def returnVal(self, x: int, y: int) -> int:
        if x >= 0 and x < self.maxX and y >= 0 and y < self.maxY:
            return self.grid[y][x]
        else:
            raise self.outOfBoundsException(x, y)

    # returns true if 2nd value is lower than the 1st
    def is2ndLower(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        try:
            isLower = False
            x1Height = self.returnVal(x1, y1)
            x2Height = self.returnVal(x2, y2)

            if x2Height <= x1Height:
                isLower = True

            return isLower
        except self.outOfBoundsException:
            return False

    def checkForLowPoint(self, x: int, y: int) -> bool:
        above = self.is2ndLower(x, y, x, y-1)
        below = self.is2ndLower(x, y, x, y+1)
        left = self.is2ndLower(x, y, x-1, y)
        right = self.is2ndLower(x, y, x+1, y)

        if above or below or left or right:
            return False
        else:
            return True


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
        for j, _ in enumerate(yList):
            if heightMap.checkForLowPoint(j, i):
                totalLowPoints += heightMap.grid[i][j] + 1
                print(heightMap.grid[i][j])
    print(totalLowPoints)


if __name__ == '__main__':
    main()
