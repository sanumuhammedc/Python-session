fruits = ['apple', 'banana', 'orange', 'grapes', 'pineapple']

print(fruits[0])
# length of list
print(len(fruits))

# add element to list
fruits.append('mango')

# add element to list at specific index
fruits.insert(1, 'watermelon')

# remove element from list
fruits.remove('banana')

# remove element from list at specific index
fruits.pop(1)


for fruit in fruits:
    print(fruit)