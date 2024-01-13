x=int(input("enter number"))
for i in range(1,x+1):
    print(" "*(x-i),end="")
    print(" *"*i)
for k in range(x-(x//2)):
    print(" "*(x-1),end="")
    print(" * ")
