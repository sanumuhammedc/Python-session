def evenodd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter a number: "))
result = evenodd(num)
print(result)