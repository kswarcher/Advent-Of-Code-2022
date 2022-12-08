def day6():

    fileInfo = open("AOC22D6P1.txt", 'r')

    count = 14
    totLetters = count
    letterArr = []

    for i in range(count):
        letterArr.append('')
    for line in fileInfo:
        for letter in line:
            letterArr.pop(0)
            letterArr.append(letter)
            if len(set(letterArr)) == len(letterArr) and letterArr[0] != '':
                print(count-totLetters + 1)
                break
            else:
                count+=1


day6()

"""
def day6():

    fileInfo = open("AOC22D6P1.txt", 'r')

    count = 4
    letterArr = []

    for i in range(count):
        letterArr.append('')
    for line in fileInfo:

        for letter in line:
            letterArr.pop(0)
            letterArr.append(letter)
            if len(set(letterArr)) == len(letterArr) and letterArr[0] != '':
                print(count-3)
                break
            else:
                count+=1


day6()
"""