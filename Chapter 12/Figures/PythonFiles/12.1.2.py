# Read file contents
print('Reading in data...')
f = open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.1.2.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average...')
total = 0
for ln in lines:
    total += int(ln)

# Compute result
avg = total/len(lines)
print('Average value:', avg)