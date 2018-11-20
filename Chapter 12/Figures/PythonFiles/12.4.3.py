f = open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\PythonFiles\\ball.bmp', 'rb')  # Open in binary mode using 'b'

# Read image binary data
contents = f.read()

print('Contents of ball.bmp\n')
print(contents)

f.close()