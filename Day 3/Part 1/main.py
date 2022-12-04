def ruckSacks():
    # read file in and set sum of priorities to 0
    fileInfo = open("AOC22D3P1.txt", 'r')
    totPriority = 0
    elfNum = 1

    # increments the value of the score for how many points were earned
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

            for letter in line1:
                if(letter in line2 and letter in line3 and not found):
                    #print(letter, line1,line2,line3)
                    if (ord(letter) < 91):
                        totPriority += ord(letter) - 38
                        found=True

                    if (ord(letter) > 91):
                        totPriority += ord(letter) - 96
                        found=True

    print(totPriority)
"""
        found = False
        for letter in firstPouch:

            if(letter in secondPouch and not found):
                if(ord(letter) < 91):
                    found = True
                    totPriority += ord(letter)-38

                if (ord(letter) > 91):
                    found = True
                    totPriority += ord(letter) - 96
"""





ruckSacks()
"""
def ruckSacks():
    # read file in and set sum of priorities to 0
    fileInfo = open("AOC22D3P1.txt", 'r')
    totPriority = 0

    # increments the value of the score for how many points were earned
    for line in fileInfo:
        firstPouch = line[:len(line)//2]
        secondPouch = line[len(line)//2:]
        found = False
        for letter in firstPouch:

            if(letter in secondPouch and not found):
                if(ord(letter) < 91):
                    found = True
                    totPriority += ord(letter)-38

                if (ord(letter) > 91):
                    found = True
                    totPriority += ord(letter) - 96


    print(totPriority)



"""