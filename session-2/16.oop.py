class MyClass():
    def __init__(self, a, b):
        self.num1 =  a
        self.num2 = b
        print("Constructor is called")

    def add(self):
         print(self.num1 + self.num2)
    

val = MyClass(10, 20)

val.add()

lis1 = [1, 2, 3, 4, 5]
lis1.append(6)


