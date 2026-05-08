def print_pattern_A(rows):
    """
    Prints the letter 'A' pattern using asterisks.
    """
    for i in range(rows):
        for j in range(rows // 2 + 1):
            if ((j == 0 or j == rows // 2) and i != 0) or \
               (i == 0 and j != 0 and j != rows // 2) or \
               (i == rows // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print() 
num_rows = 7 
print_pattern_A(num_rows)
