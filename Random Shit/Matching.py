import random

def gen_nums():
    nums = []
    for i in range(8):
        nums.append(random.randint(0, 100))
    # print("New nums:\n", nums)
    return nums

def place_nums(nums):
    nums.extend(nums)
    # print("Doubled nums:\n", nums)
    new_matrix = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
    # print("Empty Matrix:\n", new_matrix)
    for num in nums:
        col = random.randint(0,3)
        row = random.randint(0,3)
        while new_matrix[row][col] != ' ':
            col = random.randint(0,3)
            row = random.randint(0,3)
        else:
            new_matrix[row][col] = num
    return new_matrix

for i in range(10):
    print(place_nums(gen_nums()))