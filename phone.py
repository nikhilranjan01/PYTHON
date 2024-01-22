def print_phone_pattern():
    pattern = [
        '1', '2ABC', '3DEF',
        '4GHI', '5JKL', '6MNO',
        '7PQRS', '8TUV', '9WXYZ',
        '*', '0', '#'
    ]

    for row in range(4):
        for col in range(3):
            key = row * 3 + col
            print(f"{pattern[key]:<5}", end=' ')
        print()

# Call the function to print the phone pattern
print_phone_pattern()
