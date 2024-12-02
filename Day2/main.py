

def exercise_01(input):
    nb_safe = 0
    with open(input, 'r') as file:
        lines = file.readlines()
        unsafe_lines = []
        for line in lines:
            values = line.split(" ")
            is_safe = analyze_line(values)
            if is_safe:
                nb_safe+=1
            else:
                unsafe_lines.append(values)
    return nb_safe, unsafe_lines

def analyze_line(values):
    increase = False
    decrease = False
    is_safe = True
    for i in range(len(values)-1):
        if ((int(values[i])<int(values[i+1]))):
            increase = True
            if decrease:
                is_safe = False
                break       
        if ((int(values[i])>int(values[i+1]))):
            decrease =True
            if increase:
                is_safe = False
                break
        if (int(values[i])==int(values[i+1])):
            is_safe = False
            break
        if (abs(int(values[i])-int(values[i+1]))>3):
            is_safe = False
            break
    return is_safe

def exercise_02(input):
    nb_safe,unsafe_lines = exercise_01(input)
    print(nb_safe)
    nb_safer_solution = 0
    for line in unsafe_lines:
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            #print(new_line)
            is_safe = analyze_line(new_line)
            if is_safe:
                nb_safer_solution+=1
                break
    return nb_safer_solution + nb_safe

def main():
    print(exercise_02("input_day2_ex1.txt"))
    #print(exercise_02("input_day1_ex1.txt"))

if __name__ == "__main__":
    main()
