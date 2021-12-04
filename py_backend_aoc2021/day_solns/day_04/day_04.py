from typing import List

#class BingoBoard:


def main():
    f = open("./inputTest.txt", "r", encoding='utf8')

    rawString = f.read()

    calledNumsStr: str = rawString.splitlines()[0]
    boardsStr: List[str] = rawString.splitlines()[1:]

    calledNums: List[int] = list(map(int, calledNumsStr.split(',')))

    #boards: List[str] = boardsStr.split('\n\n')
    boards: List[str]
    

    print(calledNums)
    print(boardsStr)
    



if __name__ == '__main__':
    main()
