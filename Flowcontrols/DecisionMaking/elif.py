#no1=int(input("enter value for no1"))
#no2=int(input("enter value for no2"))

#if(no1<no2):
#    print("max=no2")
#elif(no1>no2):
#    print("max=no1")
#else:
#    print("both are equal")


no1=int(input("enter value for no1"))
no2=int(input("enter value for no2"))
no3=int(input("enter value for no3"))

if(no1>no2&no1>no3):
    print("max=no1")
elif(no2>no1&no2>no3):
    print("max=no2")
else:
    print("max=no3")