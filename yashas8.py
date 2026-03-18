class MyError(Exception):
    pass

try:
    raise MyError("Custom error occured")
except MyError as e:
    print(e)
