def rockPaperScissors():
    # read file in and set score to 0
    fileInfo = open("AOC22D2P1.txt", 'r')
    score = 0

    # increments the value of the score for how many points were earned
    for line in fileInfo:
        match line:
            case "A X\n":
                score += 3
            case "A Y\n":
                score += 4
            case "A Z\n":
                score += 8
            case "B X\n":
                score += 1
            case "B Y\n":
                score += 5
            case "B Z\n":
                score += 9
            case "C X\n":
                score += 2
            case "C Y\n":
                score += 6
            case "C Z\n":
                score += 7
            case _:
                print(line)

    print(score)


rockPaperScissors()