# Figure 12.1.1
print('Opening file 12.1.1.txt.')
f = open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.1.1.txt')  # create file object

print('Reading file 12.1.1..txt.')
contents = f.read()  # read file text into a string

print('Closing file 12.1.1.txt.')
f.close()  # close the file

print('\nContents of 12.1.1.txt:\n', contents)