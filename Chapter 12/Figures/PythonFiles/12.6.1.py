print('Opening myfile.txt')

# Open a file for reading and appending
with open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.6.1.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')