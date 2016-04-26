def main():
    iteration=getiteration()
    getname(iteration)
    #getcolor(iteration)
    print(iteration)


def getiteration():
    return int(input("How many people and their favorite color are you going to enter?"))


def getname(n):

    namelist=[]
    for a in range(0,n):
        firstname=input("Enter first name")
        namelist.append(firstname)
        print(a)




#def getcolor(c):

main()
