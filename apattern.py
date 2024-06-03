def print_A_pattern(height):
    if height < 3:
        print("Height should be 3 or more.")
        return
    width = height // 2 + height % 2
    for i in range(height):
        for j in range(height):
            if (j == 0 or j == height - 1) and i != 0:
                print("*", end="")
            elif i == 0 and j > 0 and j < height - 1:
                print("*", end="")
            elif i == height // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
print_A_pattern(7)
