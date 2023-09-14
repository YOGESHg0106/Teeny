arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
d=int(input("enter d : "))
c=(arr[d:])+(arr[:d])
print(c)