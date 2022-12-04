def assignmentPairs():
    # read file in and set number of assignements contained to 0
    fileInfo = open("AOC22D4P1.txt", 'r')
    assignmentsContained = 0

    # goes through the each line of the file, get sthe nubmers in each line, and finds if one range is completely in the other
    for line in fileInfo:
        num1 = int(line.split(',')[0].split('-')[0])
        num2 = int(line.split(',')[0].split('-')[1])
        num3 = int(line.split(',')[1].split('-')[0])
        num4 = int(line.split(',')[1].split('-')[1])
        if((num1 >= num3 and num1 <= num4 and num2 >= num3 and num2 <= num4) or (num3 >= num1 and num3 <= num2 and num4 >= num1 and num4 <= num2)):
            assignmentsContained += 1

    print(assignmentsContained)

assignmentPairs()