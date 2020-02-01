no1=int(input("Enter the first no:"))
no2=int(input("Enter the second no:"))
no3=int(input("Enter the third no:"))

if(((no1>no2)&(no1<no3))|((no1<no2)&(no1>no3))):
    print("no1 is the second largest no")
elif(((no2>no1)&(no2<no3))|((no2<no1)&(no2>no3))):
    print("no2 is the second largest no")
elif(((no3>no1)&(no3<no2))|((no3<no1)&(no3>no2))):
    print("no3 is the second largest no")