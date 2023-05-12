class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def print_details(self):
        print("Name: ", self.name)
        print("Course: ", self.course)

obj1 = Student("john", "python")
obj2 = Student("doe", "java")

print(obj1.print_details())

print(obj2.print_details())


