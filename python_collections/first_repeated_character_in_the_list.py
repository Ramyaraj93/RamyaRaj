char = 'acbdc'
temp = {}
for i in char:
    if i in temp:
        print(i)
        break
    else:
        temp[i]= 1