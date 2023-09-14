arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
a=int(input("element to search: "))
if a in arr:
    print(a,"exist in list")
else:
    print("get lost")