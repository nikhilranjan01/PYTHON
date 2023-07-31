'''                                                     #EXPERMIN:1 BY BHAWHANI SIR    

#Q.1 To find date and time in python
 To find out python version
import sys
print(sys.version)

#Q.2  To find date and time in python
import datetime
current_time = datetime.datetime.now()
print(current_time)

#  Second way
import datetime
current_time = datetime.datetime.now()
print("Print your input")
print("Day :", current_time.day)
print("Month :", current_time.month)
print("Year:", current_time.year)
print("Hour :", current_time.hour)
print("Minute :", current_time.minute)
print("Second :", current_time.second)
print("Microsecond :", current_time.microsecond)

#Q.3  To findout area of a circle
r=int(input("Enter Radius:"))
print("Radius of circle:",r)
print("Area of circle:",3.14*r*r)
print("perimeter of circle:",2*3.14*r)

#Q.4   Write a Python program that accepts an integer (n) and computes the value of n+ nn+ nnn.
n=int(input("enter a number:"))
print(n+n*n+n*n*n)

#Q.5   Write a Python program to calculate number of days between two dates
print("enter any date in dd/mm/yyyy format")
print("enter first date")
day,month,year=[int(n) for n in input("enter date:").split("/")]
print("enter second date")
new_day,new_month,new_year=[int(n) for n in input("enter date:").split("/")]
print(day-new_day,"days")

# Q.6. Write a Python program to swap two variables.
n1,n2=input("enter two numbers").split()
print(f"Before swapping: n1={n1} n2={n2}")
t=n1
n1=n2
n2=t
print(f"After swapping: n1={n1} n2={n2}")'''

# We have learnt about python shell, different IDE(Integrated developement environments),input/output statement, split functions in c.

                                                #EXPERMENT:2 BY BHAWHANI SIR

'''n=float(input("enter a number?"))
x=n-17
if x>17:
 print(abs(2*x))    

#Q.1.  Write a Python program to test whether the input number is near 100 or 1000 or 2000.
n=int(input("enter a number:"))
if n<500:
 print("number is nearest to 100")
elif n>500 and n<1500:
 print("number is nearest to 1000")
elif n>1500:
 print("number is nearest to 2000")
elif n==500:
 print("Numbere is nearest to both 100 and 1000")
elif n==1500:
 print("Number is nearest to both 1000 and 2000")

#  Q.2 Write a Python program to calculate the sum of three given numbers, if the values are equal then return five times of their sum.
n1,n2,n3=[float(n) for n in input("Enter three numbers").split()]
if n1==n2==n3:
 print(5*(n1+n2+n3))
else:
 print(n1+n2+n3)                              

# Q.4. Write a Python program to compute the greatest common divisor (GCD) of two positive integers./
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


# Q.5. Write a Python program to calculate the sum of the digits in an integer.
n=input("enter a number:")
sum=0
for i in n:
    sum+=int(i)
print(sum)

# Q.6. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in function !
li=[float(n) for n in input("enter space separated numbers").split()]
max=li[0]
min=li[0]
for i in li:
   if max<i:
     max=i
     if min>i:
        min=i
print(f"Max={max}")
print(f"Min={min}")

str1="HAPPY  BIRTHDAY  TO  YOU"
str2=" ANMOL  BHAIYA 🎊  🎉 🎈  🎂  🥳  ❤️"
for i in range(100):
  if i==2:
    print(str1+str2)
  else:
    print(str1+str2)

# Q.1. Write a Python program that takes a string input and displays the string in a specific format.
print("Twinkle, twinkle, little star,\nHow I wonder what you are!")
print("\n")
print("Sab moh maya hai\n\t\tFir kyu aaya hai")

# Q.2. Write a Python program to accept a filename from the user and print its extension.
x=input("Enter name of file with its extension:")
extension=x.split(".")
print(extension[-1])

st=input("Enter a string:")
if st.startswith("nikhil love"):
 pass
else:
 st="nikhil love"+st
print(st)'''

# Discussion & comments:
# In this experiment we have learnt about string properties-string methods -string indexing and slicing

# Conclusion:
# String is immutable, indexed, iterable. Various methods and function are available to work with strings.

                                                #EXPERMENT:3 BY BHAWHANI SIR

                                                





print("Twinkle, twinkle, little star,\nHow I wonder what you are!")
print("\n")
print("Sab moh maya hai\n\tFir kyu aaya hai")
