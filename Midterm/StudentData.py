student_data = {}
class_average = 0

def gather_data():
    global student_data
    print("Press 'q' in place of a student's name to quit")
    user_op = input('\nPlease enter a student\'s name: ')
    while user_op != 'q':
        scores = []
        for i in range(1, 3):
            score = float(input("Test score %d: " % i))
            scores.append(score)
        student_data[user_op] = scores
        user_op = input('\nPlease enter a student\'s name: ')

def compute_averages():
    global student_data, class_average
    class_total = 0
    for student in student_data:
        stats = []

        test1 = student_data[student][0]
        test2 = student_data[student][1]
        stats.append(test1)
        stats.append(test2)

        student_average = (test1 + test2) / 2
        letter_grade = comput_letter_grade(student_average)
        stats.append(student_average)
        stats.append(letter_grade)

        high_score = max(test1, test2)
        stats.append(high_score)

        low_score = min(test1, test2)
        stats.append(low_score)

        class_total += student_average
        student_data[student] = stats
    class_average = class_total / len(student_data)
    
def comput_letter_grade(average):
    grade = ''
    if 90 <= average <= 100:
        grade = 'A'
    elif 80 <= average <= 89:
        grade = 'B'
    elif 70 <= average <= 79:
        grade = 'C'
    elif 60 <= average <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def print_stats():
    print("\n|   Name   |  Test 1  |  Test 2  | Average  | Grade | Highest  |  Lowest  |")
    print("|-------------------------------------------------------------------------|")
    for student in student_data:
        print("|%-10s|  %-6.2f  |  %-6.2f  |  %-6.2f  |   %s   |  %-6.2f  |  %-6.2f  |"
        % (student + ':' + '', student_data[student][0], student_data[student][1], student_data[student][2],
        student_data[student][3], student_data[student][4], student_data[student][5]))
    print("\nClass Average: %0.2f" % class_average)

if __name__ == '__main__':
    gather_data()
    compute_averages()
    print_stats()