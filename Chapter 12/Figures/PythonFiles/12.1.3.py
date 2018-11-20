f = open('../TextFiles/12.1.1.txt')

for line in f:
    for ch in line:
        print(ch, end=' ')

f.close()