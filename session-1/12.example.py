# declare an empty list and add elements to it by taking input from user
fruits = []
for i in range(5):
    fruit = input("Enter fruit name: ")
    fruits.insert(0, fruit)

print(fruits)