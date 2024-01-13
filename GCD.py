# Write a Python program to compute the greatest common divisor (GCD) of two positive integers./
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if n1>n2:
    for i in range(2,n1+1):
       if n1%i==0 and n2%i==0:
             gcd=i
else:
    for i in range(2,n2+1):
        if n1%i==0 and n2%i==0:
         gcd=i
print(f"gcd={gcd}")
print(f"lcm={(n1*n2)//gcd}") 
