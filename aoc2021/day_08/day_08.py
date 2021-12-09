from typing import List
from math import ceil
from dataclasses import dataclass
from typing import Dict
import string


@dataclass
class Display:
    signal: List[str]
    output: List[str]

    decode: Dict[int, str]

    def decodeFirstFour(self):
        for signal in self.signal:
            length = len(signal)
            if length == 2:
                self.decode.update({1: signal})
            elif length == 3:
                self.decode.update({7: signal})
            elif length == 4:
                self.decode.update({4: signal})
            elif length == 7:
                self.decode.update({8: signal})

    def decode235(self):
        # get list of elements with len == 5
        lstLen5 = [x for x in self.signal if len(x) == 5]
        # find 3
        oneLetters = set(self.decode.get(1) or '')
        for item in lstLen5:
            if set(item) >= oneLetters:
                self.decode.update({3: item})
                lstLen5.remove(item)


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
                          output=tempOutput, decode={}))

    totalSpecificValues = 0
    specificValues = [1, 4, 7, 8]

    for displays in lstDisplay:
        for output in displays.output:
            if decodeOutputToken(output) in specificValues:
                totalSpecificValues += 1

    print(totalSpecificValues)


if __name__ == '__main__':
    main()
