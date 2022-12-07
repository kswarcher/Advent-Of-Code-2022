def stackTest():

    fileInfo = open("AOC22D5P1.txt", 'r')
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []
    arrayOfStack = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
    temp = []
    initialStacks = 0
    for line in fileInfo:
        if line[0] == 'm':
            num1 = int(line.split(' ')[1])
            num2 = int(line.split(' ')[3])-1
            num3 = int(line.split(' ')[5])-1

            for i in range(num1):
                temp.append(arrayOfStack[num2].pop())
            for i in range(num1):
                arrayOfStack[num3].append(temp.pop())
        else:
            for letter in line:
                if letter != '\n':
                    arrayOfStack[initialStacks].append(letter)
            initialStacks +=1


    print(arrayOfStack)

stackTest()

""""
def stackTest():

    fileInfo = open("AOC22D5P1.txt", 'r')
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []
    arrayOfStack = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
    initialStacks = 0
    for line in fileInfo:
        if line[0] == 'm':
            num1 = int(line.split(' ')[1])
            num2 = int(line.split(' ')[3])-1
            num3 = int(line.split(' ')[5])-1

            for i in range(num1):
                arrayOfStack[num3].append(arrayOfStack[num2].pop())
        else:
            for letter in line:
                if letter != '\n':
                    arrayOfStack[initialStacks].append(letter)
            initialStacks +=1


    print(arrayOfStack)

stackTest()
"""