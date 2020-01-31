f=open("/home/user/Downloads/movies.csv")
f1=open("movies.txt","w") ######### Textfile to write the output
dict={}
for data in f:
    data=data.rstrip("\n")
    data=data.split(",")
    print(data)

    year=data[2]
    print(year)
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
    print(dict)
tmp=list()
for x,y in dict.items():
    tmp.append((y,x))
tmp=sorted(tmp,reverse=True)
print("max year=",tmp[0])
tmp=sorted(tmp)
print("min year=",tmp[0])

for data in tmp:
    f1.write(str(data))
    f1.write("\n")
