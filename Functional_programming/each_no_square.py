####### to print squares of each no and print the even nos in the list

lst=[10,11,12,13,14,15,16]
print("Squares of no:")
for element in lst:
    squares=element**2
    print(squares)
print("even no are:")
for element in lst:
    if (element%2==0):
        print(element)

