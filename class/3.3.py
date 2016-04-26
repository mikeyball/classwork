

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


nummax=newlist[-1]
print(nummax)
nummin=newlist[0]
print(nummin)
#i=0
#maxnum=newlist[0]
#while i<len(newlist)-1:
    #i=i+1
   # if newlist[i]>maxnum:
        #maxnum=newlist[i]

    #print(newlist[i])
    #if newlist[i]>maxnum:
        #maxnum=newlist[i]
        #print(maxnum)


#length=len(newlist)
#print(length)


#ab=newlist[length]
#print(ab)
#length=len(newlist)
#print(length)
