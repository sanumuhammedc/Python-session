# programme to depict ecxeption handling

try:
    a = 3
    b = a/1
    
    print("Value of b = ", b)
except(ZeroDivisionError):
    print("\nError Occurred and Handled")
else:
    print("\nNo Error Occurred")
finally:
    print("\nFinally code block is always executed")    