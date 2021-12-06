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
        elif abs(self.startCoordinates.x - self.endCoordinates.x) == abs(self.startCoordinates.y - self.endCoordinates.y):
            return LineType.DIAGONAL
        else:
            return LineType.NONE

    def generatePointsList(self) -> List[Coordinates]:
        lstCoords: List[Coordinates] = []
        tempCoord: Coordinates = self.startCoordinates

        while tempCoord != self.endCoordinates:
            lstCoords.append(tempCoord)

            tempCoord = self.incPoint(tempCoord)
        
        lstCoords.append(tempCoord)

        return lstCoords
    
    def incPoint(self, oldCoord: Coordinates) -> Coordinates:
        newX: int = oldCoord.x
        newY: int = oldCoord.y

        if self.findLineType() == LineType.HORIZONTAL:
            if self.increasingX:
                newX += 1
            else:
                newX -= 1
        elif self.findLineType() == LineType.VERTICAL:
            if self.increasingY:
                newY += 1
            else:
                newY -= 1
        elif self.findLineType() == LineType.DIAGONAL:
            if self.increasingX:
                newX += 1
            else:
                newX -= 1

            if self.increasingY:
                newY += 1
            else:
                newY -= 1
        
        return Coordinates(newX, newY)

            


@dataclass
class Grid:
    gridList: List[List[int]]

    def addLine(self, lineSeg: Line):
        if lineSeg.findLineType() == LineType.HORIZONTAL or lineSeg.findLineType() == LineType.VERTICAL or lineSeg.findLineType() == LineType.DIAGONAL:
            lstPoints = lineSeg.generatePointsList()
            for point in lstPoints:
                self.gridList[point.y][point.x] += 1


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
    f = open("./input1.txt", "r", encoding='utf8')

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
