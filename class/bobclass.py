'''
def main():
    iteration=getIteration()
    getAverage(iteration)

def getIteration():
    return int(input("how many numbers will you add?"))

def getAverage(y):
    firstlist = []
    for a in range(0,y):
        testscore=int(input("Enter your test score"))
        firstlist.append(testscore)

    firstlist.append(100)
    lengthoflist=len(firstlist)
    sum=0
    for c in range(0,lengthoflist):
        sum=sum+firstlist[c]
    print(sum)

main()
'''

def main():
    iteration=getIteration()
    getAverage(iteration)

def getIteration():
    return int(input("how many numbers will you add?"))

def getAverage(y):
    firstlist = []
    for a in range(0,y):
        testscore=int(input("Enter your test score"))
        firstlist.append(testscore)


    lengthoflist=len(firstlist)
    sum=0
    print("The numbers you entered were:", end=" ")
    for c in range(0,lengthoflist):
        print(firstlist[c], end=" ")
        sum=sum+firstlist[c]
    firstlist.append(100)
    sum=sum+firstlist[lengthoflist]
    print("")
    print("The average of you number is", sum/(lengthoflist+1))


main()