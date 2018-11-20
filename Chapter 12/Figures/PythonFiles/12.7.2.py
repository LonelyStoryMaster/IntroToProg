import csv

with open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.7.1.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print('Row #%d:' % row_num, row)
        row_num += 1