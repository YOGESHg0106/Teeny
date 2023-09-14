arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
x,y=[],[]
x.extend(arr)
#print(x)
y.extend(arr)
x.sort()
y.sort(reverse=True)
if (x==arr or y==arr):
    print("yes it is monotonic")
else:
    print ("NO")