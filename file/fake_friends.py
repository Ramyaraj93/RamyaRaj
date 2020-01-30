f=open("/home/user/Downloads/fakefriends.csv")
dict={}
for words in f:
    words=words.rstrip("\n")
    words=words.split(",")
    print(words)
    age=int(words[2])
    print(age)
    if age not in dict:
        dict[age]=1
    else:
        dict[age]+=1
print(dict)
tmp=list()
for f,s in dict.items():
    tmp.append((s,f))
tmp=sorted(tmp,reverse=True)
print("max age=",tmp[0])
tmp=sorted(tmp)
print("min age",tmp[0])





