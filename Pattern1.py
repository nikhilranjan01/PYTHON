x=int(input("enter number"))
for i in range(x+3):
    if i<x:
        print(" "*(x-i),end="")
        print("*"*(2*i-1))
    else:
        print(" "*(x-1),end="")
        print("*")