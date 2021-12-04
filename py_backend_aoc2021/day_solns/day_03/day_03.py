from typing import List


def incList(l1: List[int], l2: List[int]) -> List[int]:
    for i, (_, e_l2) in enumerate(zip(l1, l2)):
        if e_l2 == 0:
            l1[i] -= 1
        elif e_l2 == 1:
            l1[i] += 1
    return l1


def totalIncList(l1: List[List[int]]) -> List[int]:
    summedList = [0] * len(l1[0])
    for row in l1:
        summedList = incList(summedList, row)
    return summedList


def gammaRate(l1: List[int]) -> List[int]:
    gamma = [0] * len(l1)
    for i, item in enumerate(l1):
        if item > 0:
            gamma[i] = 1
    return gamma


def epsilonRate(l1: List[int]) -> List[int]:
    epsilon = [0] * len(l1)
    for i, item in enumerate(l1):
        if item < 0:
            epsilon[i] = 1
    return epsilon


def toDecimal(l1: List[int]) -> int:
    x = 0
    for i, item in enumerate(l1):
        if item == 1:
            x += pow(2, (len(l1) - 1-i))
    return x


def filterAtIndex(l1: List[List[int]], index: int, value: int) -> List[List[int]]:
    temp = []
    for binlist in l1:
        if binlist[index] == value:
            temp.append(binlist)
    return temp


def returnO2Rating(l1: List[List[int]]) -> int:
    # just grab the dang length
    length = len(l1[0])

    templ1 = l1.copy()

    for i in range(length):
        x = totalIncList(templ1)

        if x[i] >= 0:
            templ1 = filterAtIndex(templ1, i, 1)
        elif x[i] < 0:
            templ1 = filterAtIndex(templ1, i, 0)

        if len(templ1) == 1:
            break

    return toDecimal(templ1[0])


def returnCO2Rating(l1: List[List[int]]) -> int:
    # just grab the dang length
    length = len(l1[0])

    templ1 = l1.copy()

    for i in range(length):
        x = totalIncList(templ1)

        if x[i] < 0:
            templ1 = filterAtIndex(templ1, i, 1)
        elif x[i] >= 0:
            templ1 = filterAtIndex(templ1, i, 0)

        if len(templ1) == 1:
            break

    return toDecimal(templ1[0])



def main():
    f = open("./input1.txt", "r", encoding='utf8')

    binaryRaw = f.read()

    lstBinary: List[str] = binaryRaw.splitlines()

    finalBinaryInt: List[List[int]] = []

    for binary in lstBinary:
        x = list(binary)
        y = []
        for item in x:
            y.append(int(item))
        finalBinaryInt.append(y)

    summedList = [0] * len(finalBinaryInt[0])

    for row in finalBinaryInt:
        summedList = incList(summedList, row)

    gamma = toDecimal(gammaRate(summedList))
    epsilon = toDecimal(epsilonRate(summedList))

    print(gamma * epsilon)

    print(returnO2Rating(finalBinaryInt) * returnCO2Rating(finalBinaryInt))


if __name__ == '__main__':
    main()
