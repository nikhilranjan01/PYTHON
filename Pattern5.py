rows = 5
for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print("* " * i)
    else:
        print("* " + " " * (2 * (i - 2)) + "* ")
