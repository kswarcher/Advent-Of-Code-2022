def ruckSacks():
    # read file in and set sum of priorities to 0
    fileInfo = open("AOC22D3P1.txt", 'r')
    totPriority = 0

    # cuts the string in half, goes through the first half, and checking every letter against the second string
    for line in fileInfo:
        firstPouch = line[:len(line)//2]
        secondPouch = line[len(line)//2:]
        found = False
        for letter in firstPouch:

            # if the letter has not been found it adds the priority of the letter (item) to the total priority
            if(not found and letter in secondPouch):
                if(ord(letter) < 91):
                    found = True
                    totPriority += ord(letter)-38

                if (ord(letter) > 91):
                    found = True
                    totPriority += ord(letter) - 96


    print(totPriority)

ruckSacks()
