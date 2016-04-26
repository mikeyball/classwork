'''
def main():
    try:
        x=input("give me your age")
        print(x+5)
    except:
        print("Why you don't give me number")
main()
'''
def main():
    newlist=[]
    try:
        x=input("give me your age")
        newlist.append(x)
        print(newlist[4])
    except:
        print("Why you don't give me number")
main()