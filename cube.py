def cube_number_pattern(size):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            for k in range(1, size + 1):
                cube = i * j * k
                print(f"{cube:4}", end=" ")
            print()
        print()

# Adjust the size parameter to change the dimensions of the cube
cube_number_pattern(4)
