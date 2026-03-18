try:
    a=10
    b=5
    result=a/b
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Result:",result)
