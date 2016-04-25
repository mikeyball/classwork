exit = False
list=[]
while (exit == False):
    x=input("Give me a number to sort")
    list.append(x)
    decision = input("press q to quit, all other input continues inputs")
    if decision == "q" or decision == "quit":
        exit = True

newlist=[]
while list:
    num=list[0]
    for y in list:
        if y<num:
            num=y
    newlist.append(num)
    list.remove(num)
print(newlist)

