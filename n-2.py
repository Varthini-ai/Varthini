def print_hollow_square(size=5):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('o', end='')
            else:
                print(' ', end='')
        print()
print_hollow_square()
