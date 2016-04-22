def main():
    v="What is the value of "
    i="Invalid Input. Please enter a numeral"
    on=True
    while(on==True):
        try:
            a=int(input(v+"a?"))
            on=False
        except:
            print(i)
    on=True
    while (on==True):
        try:
            b=int(input(v+"b?"))
            on=False
        except:
            print(i)
    on=True
    while(on==True):
        try:
            c=int(input(v+"c?"))
            on=False
        except:
            print(i)
    on=True
    while(on==True):
        try:
            x=int(input(v+"x?"))
            on=False
        except:
            print(i)
    xx=int(x*x)
    q="The following quadratic was entered: "
    if b<0:
        if c>0:
            print(q,a,"X2","^",b,"X","+",c,sep='')
        if c<0:
            print(q,a,"X2","^",b,"X",c,sep='')
    if b>0:
        if c>0:
            print(q,a,"X2","^","+",b,"X","+",c,sep='')
        if c<0:
            print(q,a, "X2","^","+",b,"X",c,sep='')
    print("The value of the quadratic is ",a*xx+b*x+c)
main()
