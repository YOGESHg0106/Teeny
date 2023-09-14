arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
pos1=int(input("enter a pos1 : "))
pos2=int(input("enter a pos2 : "))
arr[pos1],arr[pos2]=arr[pos2],arr[pos1]
print(arr)