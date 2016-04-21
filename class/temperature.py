
def main():

    x=ftemp()
    ctemp(x)

def ftemp():
    return int(input("Enter the temperature in Fahrenheit"))

def ctemp(a):
    temp=(a-32)/1.8
    print(temp,"C")
    print(a,"F")
    go=str(input("Would you Like to continue?"))
    if go=="yes":
        print("Let's go again")
        x=ftemp()
        ctemp(x)
    if go=="no":
        print("goodbye")

main()





