try:
    f=open("data.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Execution completed")
     
