# ####### to print squares of each no and print the even nos in the list
#
lst=[10,11,12,13,14,15,16]
#
# def squares(no):
#     return no**2
#
# square=list(map(squares,lst))
# print("squares=",square)
#
# def even(no):
#     return no%2==0
#
# even=list(filter(even,lst))
# print("even=",even)

f=lambda no:no**2
square=list(map(f,lst))
print("squares=",square)

square=list(map(lambda no:no**2,lst))


