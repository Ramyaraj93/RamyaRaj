
import re
x='\s'######### checking for space
#x='\d'########### CHECKING FOR digit
#x='\D' ##############non digit
x='\w'   ############ all words except spcl character
x='\W'  ########### all words and spcl characters

matcher=re.finditer(x,'a7 @Ak9z')
for match in matcher:

    print("match available at",match.start())
    print("group=",match.group())