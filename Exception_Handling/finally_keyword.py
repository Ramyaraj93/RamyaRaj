no1=int(input("Enter the no:"))
no2=int(input("Enter the no:"))
lst=[10,20,30]
try:
    res=no1/no2
    print(res)

    print("i have one db transaction")
    print("i have commit")
except Exception as e:
    no2=int(input("Enter the no2:"))
    try:
        res = no1 / no2
        print(res)
    except Exception as e:
        print(e.args)

finally:
    print("inside finally block")



