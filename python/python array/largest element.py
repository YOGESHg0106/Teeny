def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if(arr[i]>max):
            max=arr[i]
    return max

arr=[2,25,59,3,6,500,22,5,6,4,152,1,52,64]
n = len(arr)
ans=largest(arr,n)
print("the largest element is:",ans)