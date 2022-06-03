File_extention = ['py', 'c', 'c++']
Filename=input("Input the Filename: ")
for i in File_extention:
    if (Filename=='py'):
        print("The extention of the file is: Python")
        break
    elif (Filename=='c'):
       print("The extention of the file is: C")
       break
    elif(Filename=='c++'):
        print("The extention of the file is: C++")
        break
    else:
        print("Invalid Extention")
