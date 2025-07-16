size = int(input("Enter the size of the pattern: "))
row_count = 0
while row_count < size:
    # Use a for loop to print asterisks side by side for the current row.
    for i in range(size):
        # Print an asterisk without a newline character at the end.
        print("*", end="")

    # After printing all asterisks for the current row, print a newline character
    # to move to the next line for the next row.
    print()

    # Increment the row counter to move to the next row in the while loop.
    row_count += 1