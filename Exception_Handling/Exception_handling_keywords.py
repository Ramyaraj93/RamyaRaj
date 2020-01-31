no1=int(input("Enter the no:"))
no2=int(input("Enter the no:"))

try:
    res=no1/no2
    print(res)
    print("i have one db transaction")
    print("i have commit")
except:
    print("exception occured")
