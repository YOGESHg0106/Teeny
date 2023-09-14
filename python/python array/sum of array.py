def sum(arr):
    sum=0
    for i in arr :
        sum= sum+i
    return sum  
arr = [int(x) for x in input("Enter space-separated numbers: ").split()]
ans=sum(arr)     
print("sum of arr is:",ans)