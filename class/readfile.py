def main():
    f=open("read.txt","r")
    myList=[]
    for line in f:
        myList.append(line)
    b=len(myList)
    for a in range(0,b):
        print(myList[a])

main()

def readfilearg():
    validfile=False
    while validfile==False:
        try:
            file=sys.argv[1]
            f=open(read.txt,"r")