from typing import List, NamedTuple, Tuple
from enum import Enum
from dataclasses import dataclass


class LineType(Enum):
    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3


class Coordinates(NamedTuple):
    x: int
    y: int


@dataclass
class Line:
    startCoordinates: Coordinates
    endCoordinates: Coordinates

    increasingX: bool = False
    increasingY: bool = False

    def findLineType(self) -> LineType:
        # horizontal
        if self.startCoordinates.x == self.endCoordinates.x:
            return LineType.VERTICAL
        elif self.startCoordinates.y == self.endCoordinates.y:
            return LineType.HORIZONTAL
        elif abs(self.startCoordinates.x - self.endCoordinates.x) == abs(self.startCoordinates.y == self.endCoordinates.y):
            return LineType.DIAGONAL
        else:
            return LineType.NONE

    def generatePointsList(self) -> List[Coordinates]:
        lstCoords: List[Coordinates]
        tempCoord: Coordinates = self.startCoordinates

        while tempCoord != self.endCoordinates:
            if self.findLineType() == LineType.HORIZONTAL:
                tempCoord = Coordinates(tempCoord.x + 1, tempCoord.y)
            elif self.findLineType() == LineType.VERTICAL:
                tempCoord = Coordinates(tempCoord.x, y)

        return lstCoords


@dataclass
class Grid:
    gridList: List[List[int]]

    def addLine(self, lineSeg: Line):
        return

    def linesIntersect(self) -> int:
        totalIntersections: int = 0
        for rows in self.gridList:
            for cols in rows:
                if cols > 1:
                    totalIntersections += 1
        return totalIntersections


def maxGridVals(lstCoords: List[Coordinates]) -> Tuple[int, int]:
    maxX: int = 0
    maxY: int = 0
    for coord in lstCoords:
        if coord.x > maxX:
            maxX = coord.x
        if coord.y > maxY:
            maxY = coord.y
    return (maxX, maxY)


def main():
    f = open("./inputTest.txt", "r", encoding='utf8')

    rawString = f.read()

    # wrangle the data
    lstLines: List[Line] = []
    lineString: List[str] = rawString.splitlines()
    allCoords: List[Coordinates] = []

    for stringline in lineString:
        tokens = stringline.split(' -> ')
        startCoordChars = tokens[0].split(',')
        endCoordChars = tokens[1].split(',')

        allCoords.append(Coordinates(
            int(startCoordChars[0]), int(startCoordChars[1])))
        allCoords.append(Coordinates(
            int(endCoordChars[0]), int(endCoordChars[1])))

        tempLine: Line = Line(startCoordinates=Coordinates(int(startCoordChars[0]), int(
            startCoordChars[1])), endCoordinates=Coordinates(int(endCoordChars[0]), int(endCoordChars[1])))

        if tempLine.startCoordinates.x < tempLine.endCoordinates.x:
            tempLine.increasingX = True
        if tempLine.startCoordinates.y < tempLine.endCoordinates.y:
            tempLine.increasingY = True

        lstLines.append(tempLine)

    gridSize: Tuple[int, int] = maxGridVals(allCoords)

    grid: Grid = Grid(gridList=([[0] * (gridSize[0]+1)
                      for _ in range(gridSize[1] + 1)]))

    for line in lstLines:
        grid.addLine(line)

    print(grid.linesIntersect())


if __name__ == '__main__':
    main()
