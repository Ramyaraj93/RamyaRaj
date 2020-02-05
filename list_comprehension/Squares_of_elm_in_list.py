# #lst=[10,15,20,25,30,34,40]
# values=[item**2 for item in lst]
# print(values)
#
# even=[item for item in lst if item%2==0]
# print(even)

lst1=[1,2,3]
lst2=[4,5,6]
val=[(item1,item2) for item1 in lst1 for item2 in lst2]
print(val)

lst1=[1,2,3]
lst2=[4,5,6]
val=[(item1+item2) for item1 in lst1 for item2 in lst2]
print(val)
