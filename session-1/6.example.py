# number < 100 -> less than 100

# if number between 100 and 200 -> between 100 and 200
# if number between 200 and 300 -> between 200 and 300
# if number > 300 -> greater than 300

num = int(input("Enter a number: "))

if num < 100:
    print("less than 100")
elif num >= 100 and num < 200:
    print("between 100 and 200")
elif num >= 200 and num < 300:
    print("between 200 and 300")
else:
    print("greater than 300")   