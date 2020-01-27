f=open("/home/user/RamyaRaj/file/num","r")
lst=list()

for data in f:
    #print(data)
    if(int(data)%2==0):
        lst.append(data.rstrip("\n"))
print(lst)

