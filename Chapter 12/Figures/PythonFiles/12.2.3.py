import os

f = open('../TextFiles/12.2.3.txt', 'w')

f.write('Write me to a file, please!')

f.flush()
os.fsync(f.fileno())