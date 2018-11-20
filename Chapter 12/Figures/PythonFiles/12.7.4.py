import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open('F:\\CIS1415\\IntroToProgramming\\Chapter 12\\Figures\\TextFiles\\12.7.4.csv', 'w') as csvfile:
    grades_writer = csv.writer(csvfile)

    grades_writer.writerow(row1)
    grades_writer.writerow(row2)

    grades_writer.writerows([row1, row2])