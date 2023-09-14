arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
arr[0],arr[-1]=arr[-1],arr[0]
print(arr)

'''def swapList(a):
     
    a[0], a[-1] = a[-1], a[0]
 
    return a
     
# Driver code
a = [12, 35, 9, 56, 24]
print(swapList(a))'''