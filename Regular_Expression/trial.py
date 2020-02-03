import re
item=input("Enter the reg_no:")
rule="KL[0-9]{2}[A-Z]{2}[0-9]{4}"
matcher=re.fullmatch(rule,item)
if(matcher!=None):
    print("valid")
else:
    print("invalid")
