from typing import List, NamedTuple


class Instruction (NamedTuple):
    direction: str
    val: int


class Coordinates(NamedTuple):
    hori: int
    vert: int
    aim: int


def coordinateUpdate(i: Instruction, p: Coordinates) -> Coordinates:
    if i.direction == 'forward':
        newCoords = Coordinates(p.hori+i.val, p.vert + p.aim * i.val, p.aim)
    elif i.direction == 'up':
        newCoords = Coordinates(p.hori, p.vert, p.aim - i.val)
    elif i.direction == 'down':
        newCoords = Coordinates(p.hori, p.vert, p.aim + i.val)
    else:
        newCoords = p

    return newCoords


def main():
    f = open("./input1.txt", "r", encoding='utf8')

    instructionsRaw = f.read()

    lstRawInstructions: List[str] = instructionsRaw.splitlines()

    parsedInstructions = [Instruction]

    for instruction in lstRawInstructions:
        dirvalpair = instruction.split()

        parsedInstructions.append(Instruction(
            dirvalpair[0], int(dirvalpair[1])))

    baseCoords = Coordinates(0, 0, 0)

    for instruction in parsedInstructions:
        baseCoords = coordinateUpdate(instruction, baseCoords)

    print(baseCoords.vert * baseCoords.hori)


if __name__ == '__main__':
    main()
