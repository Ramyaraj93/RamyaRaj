f=open("/home/user/Downloads/movies.csv")
dict={}
for data in f:
    data=data.rstrip("\n")
    words=data.split(",")
    print(words)

    year=int(words[2])
#print(year)
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict)
tmp=list()
for f,s in dict.items():
    tmp.append((s,f))


