f=open("/home/user/RamyaRaj/file/abc")

dict={}
for data in f:
    data=data.rstrip("\n")
    words=data.split(" ")

    print(words)


    for word in words:
        if (word not in dict):
            dict[word] = 1

    else:
        dict[word] += 1
for item in dict:
    print(item, end=",")
    print(dict[item])



