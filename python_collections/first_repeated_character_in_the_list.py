st="ABBABCDA"
for elm in st:
    print(elm)

low=0
upper=low+1

while(upper>low):
    if(elm[low]!=elm[upper]):
        upper+=1
        print("new upper",upper)
    elif(elm[low]==elm[upper]):
        print("first repeat=", elm[low])
    low=low+1