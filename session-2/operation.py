from module import add, sub, mul, div

def do_operation(a, b):
    print("Choose operation: ")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")

    choice = input("Enter choice: ")  
      
    if choice == '1':
        return add(a, b)
    elif choice == '2':
        return sub(a, b)
    elif choice == '3':
        return mul(a, b)
    elif choice == '4':
        return div(a, b)
    else:
        print("Invalid choice")
