class A():
    a = 10
    b = 20


class B(A):
    c = 30
    d = 40


obj_b = B()
print("Object of class B")
print(obj_b.a)
print(obj_b.b)
print(obj_b.c)
print(obj_b.d)

obj_a = A()
print("Object of class A")
print(obj_a.a)
print(obj_a.b)
