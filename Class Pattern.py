'''x=int(input("enter number"))
for i in range(1,x+1):
    print(" "*(x-i),end="")
    print(" *"*i)
for k in range(x-(x//2)):
    print(" "*(x-1),end="")
    print(" * ")

# second question:

x=int(input("enter number"))
for i in range(x+3):
    if i<x:
        print(" "*(x-i),end="")
        print("*"*(2*i-1))
    else:
        print(" "*(x-1),end="")
        print("*")

# Third question:

l=[3,5,7,8,9,3]
ans=0
for i in l:
    ans=ans^i
print(ans)'''

list=[2,4,6,2,4,9,8,8,9]
k=len(list)
list.sort()
i=0
while i<k-1:
    if list[i]==list[i+1]:
        i+=2
    else:
        print(list[i])
        break
    if(i==k-1):
        print(list[i])



 