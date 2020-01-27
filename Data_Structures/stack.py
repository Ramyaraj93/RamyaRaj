stk=[]
limit=int(input("Enter the limit"))
no=1

def push(n):
    print(n,"inside stack")

def pop():
    print(stk[-1],"popped out")

def display():
    print(stk)

while(no!=0):
    option=int(input("enter 1 for push,2 for pop,3 for dis"))
    if(option==1)&(len(stk)<limit):
        n=int(input("enter num="))
        push(n)
        stk.append(n)
        print(stk)
    else:
        print("stack is full")
    if(option==2):
        if stk==[]:
            print("empty stack,can't pop item")
        else:
            pop()
    elif(option==3):
        display()
    no=int(input("do you want to continue press 1,press 0 for exit"))



