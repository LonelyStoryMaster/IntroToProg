num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open('../TextFiles/12.2.2.txt', 'w')
f.write(str(num1))
f.write(' + ')
f.write(str(num2))
f.write(' = ')
f.write(str(num3))
f.close()