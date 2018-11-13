f = open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.1.1.txt')

for line in f:
    for ch in line:
        print(ch, end=' ')

f.close()