# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
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