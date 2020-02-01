#### to find the even no:s b/w a range

LL=int(input("Enter the lower limit:"))
UL=int(input("Enter the upper limit:"))

for i in range(LL,UL+1):
    if(i%2==0):
        print(i)