class A():
    a = 10
    b = 20
    def __init__(self):
        print("Constructor of class A is called")

class B(A):
    c = 30
    d = 40
    def __init__(self):
        super().__init__()
        print("Constructor of class B is called")        


obj_b = B()