

try:
    file=open("Ramya.txt")
    for data in file:
        print(data)
except Exception as e:
    print(e.args)