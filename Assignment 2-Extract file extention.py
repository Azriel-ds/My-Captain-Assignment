filename = input("Input the Filename: ")
f_extns = filename.split(".")
if f_extns[-1]=='py':
    print("The extension of the file is : Python")
elif f_extns[-1]=='c':
    print("The extension of the file is : C")

