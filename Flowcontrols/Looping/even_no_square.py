LL=int(input("Enter the lower limit:"))
UL=int(input("Enter the upper limit:"))

for i in range(LL,UL):
    if (i % 2 == 0):
        i=i*i
        print(i)