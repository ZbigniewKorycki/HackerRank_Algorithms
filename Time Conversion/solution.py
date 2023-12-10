import os


def timeConversion(s):
    if s.endswith("AM"):
        time_without_am = s.replace("AM", '')
        hours, minutes, seconds = time_without_am.split(":")
        if int(hours) == 12:
            hours = '00'
        return ":".join([hours, minutes, seconds])
    elif s.endswith("PM"):
        time_without_pm = s.replace("PM", '')
        hours, minutes, seconds = time_without_pm.split(":")
        if int(hours) != 12:
            hours = int(hours) + 12
        return ":".join([str(hours), minutes, seconds])

print(timeConversion("12:45:54PM"))
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = timeConversion(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()
