f=open("/home/user/RamyaRaj/file/num(row)","r")

lst=list()
for data in f:
    #print(data)
    numbers=data.split(",")
    for number in numbers:
        print(number)
        if(int(number)%2==0):
            lst.append(number.rstrip("\n"))
print(lst)