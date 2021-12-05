from typing import List
from dataclasses import dataclass


@dataclass
class Square:
    val: int = 0
    selected: bool = False


@dataclass
class BingoBoard:
    board: List[List[Square]]

    def selectVals(self, value: int):
        for i, rows in enumerate(self.board):
            for j, cols in enumerate(rows):
                if cols.val == value:
                    self.board[i][j].selected = True

    def sumUnmarked(self) -> int:
        sumBoard: int = 0
        for rows in self.board:
            for cols in rows:
                if cols.selected == False:
                    sumBoard += cols.val
        return sumBoard

    def winningBoard(self) -> bool:
        winningBoard = False
        for i, rows in enumerate(self.board):
            selectedCount: int = 0
            for j, cols in enumerate(rows):
                if cols.selected == True:
                    selectedCount += 1
            if selectedCount == len(rows):
                winningBoard = True

        for i, rows in enumerate(self.board):
            selectedCount: int = 0
            for j, cols in enumerate(rows):
                if self.board[j][i].selected == True:
                    selectedCount += 1
            if selectedCount == len(rows):
                winningBoard = True

        return winningBoard

def allWinners(l1:List[int]) -> bool:
    allWinners = False
    count = 0
    for l in l1:
        if l == 1:
            count += 1
    if count == len(l1):
        allWinners = True

    return allWinners



def main():
    f = open("./input1.txt", "r", encoding='utf8')

    rawString = f.read()

    calledNumsStr: str = rawString.splitlines()[0]
    boardsStr: List[str] = rawString.split('\n\n')[1:]

    calledNums: List[int] = list(map(int, calledNumsStr.split(',')))
    listBoards: List[BingoBoard] = []

    for string in boardsStr:
        thisboard: List[List[Square]] = []
        lstRows = string.splitlines()

        for row in lstRows:
            tempRow: List[Square] = []
            lstCols = list(map(int, row.split()))

            for col in lstCols:
                tempRow.append(Square(col, False))

            thisboard.append(tempRow)

        listBoards.append(BingoBoard(thisboard))

    winners:List[int] = [0]* len(listBoards)

    for num in calledNums:
        breakcondition = False
        for i, _ in enumerate(listBoards):
            listBoards[i].selectVals(num)
            if listBoards[i].winningBoard() == True:
                winners[i] = 1
                if allWinners(winners):
                    print(num, listBoards[i].sumUnmarked())
                    print(listBoards[i].sumUnmarked() * num)
                    breakcondition = True
                    break
        if breakcondition == True:
            break


if __name__ == '__main__':
    main()
