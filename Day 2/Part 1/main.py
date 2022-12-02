def rockPaperScissors():

    fileInfo = open("AOC22D2P1.txt", 'r')
    #rPSLines = fileInfo.readline()
    #print(fileInfo.read())
    score = 0
    for line in fileInfo:
        #print(line)

        match line:
            case "A X\n":
                score += 4
            case "A Y\n":
                score += 8
            case "A Z\n":
                score += 3
            case "B X\n":
                score += 1
            case "B Y\n":
                score += 5
            case "B Z\n":
                score += 9
            case "C X\n":
                score += 7
            case "C Y\n":
                score += 2
            case "C Z\n":
                score += 6
            case _:
                print(line)

    print(score)



rockPaperScissors()