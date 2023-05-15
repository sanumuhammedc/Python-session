# *
# **
# ***
# ****

input = int(input("Enter the number of rows: "))

for i in range(1, input+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    
