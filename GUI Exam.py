from tkinter import *

root = Tk()
root.title("C.I.CALCULATOR")
root.geometry("700x600")
root.resizable(width=False, height=False)

def ci_calculator():
    principal = int(principal_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())
    n = int(n_field.get())

    CI = principal * (pow((1 + rate / n), n * time))
    compound_field.delete(0, END) 
    compound_field.insert(END, CI)

label1 = Label(root, text="Principal Amount:", bg='red')
label1.grid(row=1, column=0)

label2 = Label(root, text="Rate:", bg='blue')
label2.grid(row=2, column=0)

label3 = Label(root, text="Time:", bg='green')
label3.grid(row=3, column=0)

label4 = Label(root, text="Compound Interest:", bg='pink')
label4.grid(row=5, column=0)

label5 = Label(root, text="n:", bg='yellow')
label5.grid(row=4, column=0)

principal_field = Entry(root)
rate_field = Entry(root)
time_field = Entry(root)
compound_field = Entry(root)
n_field = Entry(root)
principal_field.grid(row=1, column=1, padx=10, pady=10)
rate_field.grid(row=2, column=1, padx=10, pady=10)
time_field.grid(row=3, column=1, padx=10, pady=10)
compound_field.grid(row=5, column=1, padx=10, pady=10)
n_field.grid(row=4, column=1, padx=10, pady=10)

button1 = Button(root, text="Submit", bg="red", command=ci_calculator)
button1.grid(row=6, column=1, pady=10)
root.mainloop()