def ruckSacks():
    # read file in and set sum of priorities to 0
    fileInfo = open("AOC22D3P2.txt", 'r')
    totPriority = 0
    elfNum = 1

    # goes through each line of the file, assign every 3 lines to line1, line2, and line 3
    for line in fileInfo:
        found= False
        if(elfNum == 1):
            line1 = line
            elfNum=2
        elif (elfNum == 2):
            line2 = line
            elfNum = 3
        elif (elfNum == 3):
            line3 = line
            elfNum = 1

            # itterates through each letter in the first line, finds the matching letter for all three lines
            for letter in line1:
                if( not found and letter in line2 and letter in line3):
                    # adds the priority number to the total
                    if (ord(letter) < 91):
                        totPriority += ord(letter) - 38
                        found=True

                    if (ord(letter) > 91):
                        totPriority += ord(letter) - 96
                        found=True

    print(totPriority)


ruckSacks()
