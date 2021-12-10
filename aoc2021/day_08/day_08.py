from typing import List
from dataclasses import dataclass
from typing import Dict


@dataclass
class Display:
    signal: List[str]
    output: List[str]

    decodeKey: Dict[int, str]

    def __decode(self):
        self.__decodeFirstFour()
        self.__decodeRest()

    def __decodeFirstFour(self):
        for signal in self.signal:
            length = len(signal)
            if length == 2:
                self.decodeKey.update({1: signal})
            elif length == 3:
                self.decodeKey.update({7: signal})
            elif length == 4:
                self.decodeKey.update({4: signal})
            elif length == 7:
                self.decodeKey.update({8: signal})

    def __decodeRest(self):
        # get list of elements with len == 5
        lstLen5 = [x for x in self.signal if len(x) == 5]
        # find 3
        oneLetters = set(self.decodeKey.get(1) or '')
        for item in lstLen5:
            if set(item) >= oneLetters:
                self.decodeKey.update({3: item})
                lstLen5.remove(item)

        lstLen6 = [x for x in self.signal if len(x) == 6]
        # find 6
        for item in lstLen6:
            if set(item) >= oneLetters:
                pass
            else:
                self.decodeKey.update({6: item})
                lstLen6.remove(item)

        # find 5 and 2
        sixLetters = set(self.decodeKey.get(6) or '')
        for item in lstLen5:
            if sixLetters >= set(item):
                self.decodeKey.update({5: item})
            else:
                self.decodeKey.update({2: item})

        # find 0 and 9
        fourLetters = set(self.decodeKey.get(4) or '')
        for item in lstLen6:
            if set(item) >= set(fourLetters):
                self.decodeKey.update({9: item})
            else:
                self.decodeKey.update({0: item})

    def checkDecodeKey(self, s1: str) -> int:
        set1 = set(s1)
        placeHolder: int = -1
        for key, value in self.decodeKey.items():
            if set(value) == set1:
                placeHolder = key

        return placeHolder

    def decodeOutput(self) -> int:
        self.__decode()

        lstOutputVals: List[str] = []
        for item in self.output:
            if self.checkDecodeKey(item) != -1:
                lstOutputVals.append(str(self.checkDecodeKey(item)))

        finalOutput = int(''.join(lstOutputVals))
        print(finalOutput)

        return finalOutput


def main():
    f = open("./input1.txt", "r", encoding='utf8')

    rawString = f.read()

    lines = rawString.splitlines()

    lstDisplay: List[Display] = []

    for line in lines:
        tempSignals: List[str]
        tempOutput: List[str]

        splitLine = line.split('|')

        tempSignals = splitLine[0].split()
        tempOutput = splitLine[1].split()

        lstDisplay.append(Display(signal=tempSignals,
                          output=tempOutput, decodeKey={}))

    runningTotal = 0

    for display in lstDisplay:
        runningTotal += display.decodeOutput()

    print(runningTotal)


if __name__ == '__main__':
    main()
