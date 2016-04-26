def main():
    listprogram()

def listprogram():
    newlist=[]

    exit=False
    while(exit==False):
        newlist.append(input("What is your name?"))
        newlist.append(input("What is your color?"))
        decision=input("press q to quit, all other input continues")
        if decision=="q" or decision=="quit":
            exit=True
        length=len(newlist)
        for a in range(0,length,2):
            print(newlist[a],"Favorite Color is", end="")
            print(newlist[a+1])

main()
