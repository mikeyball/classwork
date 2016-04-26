def main():

    from random import randint
    a=randint(1,10)
    print(randint(1,10))
    print(a)

    on=True
    count=0
    while(on==True):
        count=count+1
        if count==4:
            on=False
            return
        if count<4:
            try:
                x=int(input("Enter a number from 1-10"))
                if x <= 10 and x >=1:
                    on=False
            except:
                print("You need to enter a number from 1-10")

        print(x)
        if x==a:
                print("You win")
                on=False
        elif x==(a+2) and x==(a-2):
                print("Warm")
                on=True
        elif x==(a+1) and x==(a-1):
                print("Hot")
                on=True
        else:
                print("Cold")
                on=True








main()
