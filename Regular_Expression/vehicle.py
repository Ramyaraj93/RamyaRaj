import re
fr=open("/home/user/RamyaRaj/Regular_Expression/veh_reg_no")
fw=open("/home/user/RamyaRaj/Regular_Expression/veh_write",'w')
rule='KL\d{2}[A-Z]{2}\d{4}'
for numbers in fr:
    #print(numbers)
    numbers=numbers.rstrip("\n")
    print(numbers)
    matcher=re.fullmatch(rule,numbers)
    if(matcher!=None):
        fw.write(numbers)
        fw.write("\n")
