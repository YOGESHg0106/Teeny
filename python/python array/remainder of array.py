arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
lens = len(arr)
n =int(input("enter n: "))
mul=1
for i in range(lens):
    mul=mul* arr[i]
r=mul%n
print(r)