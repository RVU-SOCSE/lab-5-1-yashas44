try:
    a=int(input("Enter number:"))
    b=int(input("Enter number:"))
    print(a/b)
except ValueError:
    print("Invalid number entered.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
