f=open("file_write_even.txt","w")
g=open("file_write_odd.txt","w")
lst=[10,15,5,25,20,30,40,50,60]

for data in lst:
    if(data%2==0):
        f.write(str(data))
        f.write("\n")
    else:
        g.write(str(data))
        g.write("\n")



