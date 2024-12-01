

def exercise_01(input):
    list1 = []
    list2 = []
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
    list1.sort()
    list2.sort()
    result = 0
    for i in range(len(list1)):
        result+=abs(list1[i] - list2[i])
    return result

def exercise_02(input): 
    list1 = []
    list2 = []
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
    #creating a dictionary 
    dict = {}
    for i in range(len(list1)):
        dict[list1[i]] = 0 
    for i in range(len(list2)):
        if list2[i] in dict:
            dict[list2[i]] += 1
    #summing the values of the dictionary
    result = 0
    for key in dict:
        result+=dict[key]*key
    return result

def main():
    print(exercise_01("input_day1_ex1.txt"))
    print(exercise_02("input_day1_ex1.txt"))

if __name__ == "__main__":
    main()
