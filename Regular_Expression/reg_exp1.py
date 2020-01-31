
import re
#count=0

#x='\w'

#x='[abc]'   ######### checks whether eaither a,b or c
#x='[^abc]'  ######### except a,b and c
x='[a-z]'   ###### a to z
x='[^a-z]'   ###### except lowercase a to z
x='[a-zA-Z]'  ##### lower case a-z & upper case A to Z(all eng alphabets)
x='[0-9]'########## check for digits
x='[a-zA-Z0-9]'  ######### all alphabets and no
matcher=re.finditer(x,'a7 @Ak9z')
for match in matcher:

    print("match available at",match.start())
    print("group=",match.group())
