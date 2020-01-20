lst=list()

limit=int(input("enter limit of list"))

for i in range(0,limit):
    val=int(input("enter value"))
    lst.append(val)

for item in lst:
    print(item)