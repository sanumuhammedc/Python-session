a = 10

print(a)

def f():
    print("Inside f()")
    globals()['a'] = 20
    print(a)


f() 
print("Outside f()")
print(a)    


class A:
    val=10


obj = A()

b = obj

b.val = 20