import re
item=input("Enter the email_id:")
rule='\w[0-9a-zA-Z]+@gmail.com'
matcher=re.fullmatch(rule,item)
if(matcher!=None):
    print("valid")
else:
    print("invalid")