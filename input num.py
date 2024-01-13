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