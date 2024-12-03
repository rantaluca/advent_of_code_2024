import re
from operator import mul

def exercise_01(input):
    with open(input, 'r') as file:
        content = file.read()
    result = re.findall('mul\(\d{1,3},\d{1,3}\)', content)
    total = 0
    for i in result:
        total+=eval(i, {"mul": mul})
    print(total)

def exercise_02(input):
    with open(input, 'r') as file:
        content = file.read()
    result = re.finditer('don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', content)
    total = 0
    is_enabled = True
    for i in result:
        str = i.group()
        #print(str)
        if str == "don't()":
            is_enabled = False
        elif str == "do()":
            is_enabled = True
        elif is_enabled:
            total+=eval(str, {"mul": mul})
    return total        

def main():
    print(exercise_02("input.txt"))
    #print(exercise_02("input_day1_ex1.txt"))

if __name__ == "__main__":
    main()
