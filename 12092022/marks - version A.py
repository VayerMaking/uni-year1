
# Analysing marks in Long Jump

def readMark(marks):
    inputMark = input("Input a mark for player A: ")
    if inputMark == "":
        return
    mark = int(inputMark)
    marks.append(mark)

def calculateMark(marks):
    if len(marks) == 0:
        highest = None
    else:
        highest = marks[0]
        for index in range(1, len(marks)):
            if marks[index] > highest:
                highest = marks[index]
    return highest

while True:
    marksA = readMark(marksA)
    marksB = readMark(marksB)
    highestA = calculateMark(marksA)
    highestB = calculateMark(marksB)

    # Calculate the winner or winners:
    if highestA == None:
        if highestB == None:
            winners = []
        else:
            winners = ["B"]
    else:
        if highestB == None:
            winners = ["A"]
        else:
            if highestA > highestB:
                winners = ["A"]
            elif highestA < highestB:
                winners = ["B"]
            else:
                winners = ["A", "B"]

    # Output the result:
    if len(winners) == 0:
        print("Nobody wins.")
    elif len(winners) == 1:
        print("Player", winners[0], "wins.")
    else:
        print("It is a tie between player", winners[0],
                "and player", winners[1] + ".")
