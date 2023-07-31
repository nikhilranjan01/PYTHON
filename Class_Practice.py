'''# Q.1
class car:
    def shiftear(self):
        print("function call ")
x=car()
x.shiftear()

# Q.2.
import string
print(string.ascii_letters)
print(type(string.digits))
la=list(string.ascii_letters)
ld=list(string.digits)
print(la)
print(ld)

# Q.3.
test_str="nikhil"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Count of all characters in GeeksforGeeks is :\n "+ str(all_freq))

# Q.4.factorial of number
x=int(input("enter number:"))
for i in range (1,x+1):
    if x%i==0:
        print(i,end=":")

# Q.4.sum=0
sum=0
x=int(input("enter number:"))
for i in range (1,x):
    if x%i==0:
        sum=sum+i
if sum==x:
    print("perfect:")
else:
    print("not perfect:")  

# Q.5.
k=int(input("Enter number:"))
while(k%2==0):
    k=k//2
if(k==1):
    print("true:")
else:
    print("false:")'''

# Q.6.
x=int(input("enter Number:"))
def cheak (x):
    if(x==0 or x%2!=0):
        return False
    if(x==1):
        return True
    return cheak(x//2)
cheak(x)    

# l=[7,8,9,1,2,3,4,5,6,7]
# x=int(input("enter number:"))
# for i in range(9):