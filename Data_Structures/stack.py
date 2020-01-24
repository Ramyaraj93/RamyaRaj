stk=[]
limit=int(input("Enter the limit"))
n=1
def push(item):
    print("inside push")

def pop():
    print("item popped out")

def display():
    print("inside display")

while(n!=0):
    option=int(input("se;ect option 1)push 2)pop 3)display"))

if(option==1):
    push(10)
elif(option==2):
    pop()
elif(option==3):
    display()

n=int(input("do you want to continue press 0 to exit"))

