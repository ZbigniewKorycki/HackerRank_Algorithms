import math
import os
import random
import re
import sys


def gradingStudents(grades):
    result = list()
    for grade in grades:
        dis_to_mult_of_five = grade % 5
        if grade < 38 or dis_to_mult_of_five < 3:
            result.append(grade)
        else:
            result.append(grade + (5 - dis_to_mult_of_five))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
