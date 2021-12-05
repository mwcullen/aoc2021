
def main():
    f=open("./input1.txt", "r", encoding='utf8')

    depthMeasurementsRaw = f.read()

    lstDepthMeasurements = depthMeasurementsRaw.splitlines()

    increaseCount = 0
    first = None
    second = None
    third = None
    lastSum = None

    for depth in lstDepthMeasurements:
        if first == None:
            first = int(depth)
        elif second == None:
            second = int(depth)
        elif third == None:
            third = int(depth)
            lastSum = first + second + third
        else:
            if lastSum == None:
                lastSum = first + second + third
            else:
                currentSum = int(depth) + second + third

                if currentSum > lastSum:
                    increaseCount += 1

                lastSum = currentSum
                first = second
                second = third
                third = int(depth)
            

    print(increaseCount)
        
    

if __name__ == '__main__':
    main()
