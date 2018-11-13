import os

f = open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.2.3.txt', 'w')

f.write('Write me to a file, please!')

f.flush()
os.fsync(f.fileno())