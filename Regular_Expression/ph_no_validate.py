import re
fr=open("/home/user/RamyaRaj/Regular_Expression/ph_nos")
fw=open("/home/user/RamyaRaj/Regular_Expression/ph_no_write",'w')
rule='[0-9]{10}'
for numbers in fr:
    #print(numbers)
    numbers=numbers.rstrip("\n")
    print(numbers)
    matcher=re.fullmatch(rule,numbers)
    if(matcher!=None):
        fw.write(numbers)
        fw.write("\n")