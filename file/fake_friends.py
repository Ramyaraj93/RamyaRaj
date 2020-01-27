f=open("/home/user/Downloads/fakefriends.csv")
dict={}
for data in f:
    data=data.rstrip("\n")
    words=data.split(",")
    print(words)

age=words[2]
print(age)
#if age is not in dict:

