no1=int(input("Enter the no:"))
no2=int(input("Enter the no:"))
lst=[10,20,30]
try:
    res=no1/no2
    print(res)

    print("i have one db transaction")
    print("i have commit")
except Exception as e:
#    print("exception occured")
    print(e.args)   ########## proper excptn msg




try:
    index=int(input("Enter index position"))
    print("your value",lst[index])
except Exception as e:
#    print("exception occured")
    print(e.args)

