a=int(input("enter a number : "))
def Fibonacci(n):
    if (n<=0):
        print('incorrect input')
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
print("the Fibonacci of ",a,"is",Fibonacci(a))
    