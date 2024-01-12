# password_generetor()
import string
import random as rand
char=string.ascii_letters +string.digits+"!@#$%^&"
l=list(char)
def password_generetor():
    pl=int(input("length of password"))
    rand.shuffle(l)
    password=[]
    for i in range(pl):
        password.append(rand.choice(l))
    rand.shuffle(password)
    password="".join(password)
    print(password)
password_generetor()
