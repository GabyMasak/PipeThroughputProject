
"""
This module contains functions for solving a pipe throughput problem.

Author: Gabriela Masak
Date: 2024-07-12
"""

textFile = 'coding_qual_input.txt'

def pipeFitter(textFile):
    # Open file and read in data, find starting point
    with open(textFile, encoding="utf-8") as f:
        lines = []
        allCoords = []
        for line in f:
            line = line.split()
            line[1] = int(line[1])
            line[2] = int(line[2])
            coords = [line[1], line[2]]
            lines.append(line)
            allCoords.append(coords)
            # print(line)
            if '*' in line:
                startLine = lines.index(line)
                xCoordinateStart = line[1]
                yCoordinateStart = line[2]
                startCoordinates = [xCoordinateStart, yCoordinateStart]
            # print(line)
        f.close()

    def coordinatesToIndex(xCoordinate, yCoordinate):
        for line in lines:
            searchX = line[1]
            searchY = line[2]
            if xCoordinate == searchX and yCoordinate == searchY:
                listIndex = lines.index(line)
                # print(listIndex)
                return listIndex

    def getCoordinates(listIndex):
        xCoordinate = lines[listIndex][1]
        yCoordinate = lines[listIndex][2]
        coordinates = [xCoordinate, yCoordinate]
        # print(coordinates)
        return coordinates

    def getPipe(listIndex):
        pipe = lines[listIndex][0]
        # print(pipe)
        return pipe

    def definePipe(pipe):

        """
        This function performs an analysis of the type of pipe and it's throughput.

        Args:
            pipe (str): The type of the pipe item.

        Returns:
            convertedBooleanSinks: Description of the return value.
        """
        if pipe == '╩':
            north = True
            west = True
            east = True
            south = False
            endPoint = False

        elif pipe == '╠':
            north = True
            west = False
            east = True
            south = True
            endPoint = False

        elif pipe == '╣':
            north = True
            west = True
            east = False
            south = True
            endPoint = False

        elif pipe == '╦':
            north = False
            west = True
            east = True
            south = True
            endPoint = False

        elif pipe == '═':
            north = False
            west = True
            east = True
            south = False
            endPoint = False

        elif pipe == '║':
            north = True
            west = False
            east = False
            south = True
            endPoint = False

        elif pipe == '╔':
            north = False
            west = False
            east = True
            south = True
            endPoint = False

        elif pipe == '╚':
            north = True
            west = False
            east = True
            south = False
            endPoint = False

        elif pipe == '╗':
            north = False
            west = True
            east = False
            south = True
            endPoint = False

        elif pipe == '╝':
            north = True
            west = True
            east = False
            south = False
            endPoint = False

        elif pipe == '*':
            north = True
            west = True
            east = True
            south = True
            endPoint = False

        else:
            north = True
            west = True
            east = True
            south = True
            endPoint = True

        # J, L, Z, F, G, W, R, B, T, D, K, V, I, *, X, C, P, U, M,

        pipeThroughput = [north, west, east, south, endPoint]
        return pipeThroughput

    def checkThroughputNorth(xCoordinate, yCoordinate):
        checkYCoord = yCoordinate + 1
        checkIndex = coordinatesToIndex(xCoordinate, checkYCoord)
        checkPipe = getPipe(currentIndex)
        checkThroughput = definePipe(currentPipe)
        if checkThroughput[3] == True:
            return True
        else:
            return False

    def checkThroughputWest(xCoordinate, yCoordinate):
        checkXCoord = xCoordinate - 1
        checkIndex = coordinatesToIndex(checkXCoord, yCoordinate)
        checkPipe = getPipe(currentIndex)
        checkThroughput = definePipe(currentPipe)
        if checkThroughput[2] == True:
            return True
        else:
            return False

    def checkThroughputEast(xCoordinate, yCoordinate):
        checkXCoord = xCoordinate + 1
        checkIndex = coordinatesToIndex(checkXCoord, yCoordinate)
        checkPipe = getPipe(currentIndex)
        checkThroughput = definePipe(currentPipe)
        if checkThroughput[1] == True:
            return True
        else:
            return False

    def checkThroughputSouth(xCoordinate, yCoordinate):
        checkYCoord = yCoordinate - 1
        checkIndex = coordinatesToIndex(xCoordinate, checkYCoord)
        checkPipe = getPipe(currentIndex)
        checkThroughput = definePipe(currentPipe)
        if checkThroughput[0] == True:
            return True
        else:
            return False

    currentCoordinates = []
    checkedCoordinates = []
    currentCoordinates.append(startCoordinates)
    xCoordinate = xCoordinateStart
    yCoordinate = yCoordinateStart
    xyCoordinates = [xCoordinate, yCoordinate]
    endPoints = []
    finalPoints = []

    while len(currentCoordinates) != 0:
        for coordinate in currentCoordinates:
            checkedCoordinates.append(coordinate)
            currentX = coordinate[0]
            currentY = coordinate[1]
            lastCoordinates = [currentX, currentY]

            currentCoordinates.remove(lastCoordinates)
            currentIndex = coordinatesToIndex(currentX, currentY)
            # print(currentIndex)
            currentPipe = getPipe(currentIndex)
            # print(currentPipe)
            currentThroughput = definePipe(currentPipe)
            # print(currentThroughput)

            # Need to check throughput of connecting pipe.
            if currentThroughput[0] == True and checkThroughputNorth(currentX, currentY) == True:
                yCoordinate = currentY + 1
                xyCoordinates = [currentX, yCoordinate]
                if yCoordinate >= 0 and xyCoordinates not in checkedCoordinates and xyCoordinates in allCoords:
                    # xyCoordinates = [currentX, yCoordinate]
                    currentCoordinates.append(xyCoordinates)
            if currentThroughput[1] == True and checkThroughputWest(currentX, currentY) == True:
                xCoordinate = currentX - 1
                xyCoordinates = [xCoordinate, currentY]
                if xCoordinate >= 0 and xyCoordinates not in checkedCoordinates and xyCoordinates in allCoords:
                    # xyCoordinates = [xCoordinate, currentY]
                    currentCoordinates.append(xyCoordinates)
            if currentThroughput[2] == True and checkThroughputEast(currentX, currentY) == True:
                xCoordinate = currentX + 1
                xyCoordinates = [xCoordinate, currentY]
                if xCoordinate >= 0 and xyCoordinates not in checkedCoordinates and xyCoordinates in allCoords:
                    # xyCoordinates = [xCoordinate, currentY]
                    currentCoordinates.append(xyCoordinates)
            if currentThroughput[3] == True and checkThroughputSouth(currentX, currentY) == True:
                yCoordinate = currentY - 1
                xyCoordinates = [currentX, yCoordinate]
                if yCoordinate >= 0 and xyCoordinates not in checkedCoordinates and xyCoordinates in allCoords:
                    currentCoordinates.append(xyCoordinates)

            if currentThroughput[4] == True:

                endPointAlpha = currentPipe
                finalPoints.append(endPointAlpha)


    return finalPoints

finalPipes = []
finalPipes = ''.join(pipeFitter(textFile))
print("The pipes lead to:", finalPipes)
