import re

def search_pattern_old(input,recursion=False):
    # if input == []:
    #     return 0 
    pattern="XMAS"
    iter_pattern = 0
    iter_input = 0
    result = 0
    while (iter_input <len(input) and iter_pattern <len(pattern)):
        
        if input[iter_input] == pattern[iter_pattern]:
            iter_input+=1
            iter_pattern+=1
        else:
            if input[iter_input] == pattern[0] and iter_pattern > 0:
                print("rec call")
                iter_input+=1
                print(input[iter_input-1:])
                result += search_pattern(input[iter_input-1:], True)
            else:
                iter_input+=1
                
        

    if iter_pattern == len(pattern):
        result+=1
        if not recursion and iter_input < len(input):
            print(recursion)
            print("moving to next" + input[iter_input:])
            result += search_pattern(input[iter_input:])
    print("returning ")
    return result  

def search_pattern(pattern,input):
    search = re.findall(pattern, input)
    result = 0
    while len(search) > 0:
        result+=len(search)
        input = re.sub(pattern, "", input)  
        search = re.findall(pattern, input)
    return result

def get_diagonals(grid):
    diagonals = []
    rows, cols = len(grid), len(grid[0])
    for d in range(-(rows - 1), cols):
        diagonals.append("".join(grid[i][i - d] for i in range(max(0, d), min(rows, cols + d))))
    for d in range(rows + cols - 1):
        diagonals.append("".join(grid[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))))

    text = ""
    for i in diagonals:
        text+=i
        
    return text

def exercise_01(input):#
    with open(input, 'r') as file:
        content = file.read()
    with open(input, 'r') as file:
        lines = file.readlines()
        without_el = []
        for i in lines: 
            without_el.append(i.replace('\n', '').replace('\r', ''))
        print(lines)
    #result = search_pattern('XMAS',content)
    #result+=search_pattern('SAMX',content)
    #rotation 90 
    new_text_90 = ""
    print(new_text_90)
    for i in range(len(without_el[0])):
        for j in range(len(without_el)):
            new_text_90 += without_el[j][i]
    result+= search_pattern('XMAS',new_text_90)
    result+=search_pattern('SAMX',new_text_90)
    #rotation 45 
    new_text_45= get_diagonals(without_el)
    print(new_text_45)
    result= search_pattern('XMAS',new_text_45)
    result+=search_pattern('SAMX',new_text_45)
    return(result)  

def main():
    test = "XMAS"
    #print(test[1:])
    #print(search_pattern("XMAS"))
    #print(search_pattern("XMASXMAS"))
    #print(search_pattern("XASXMAXXMSXXSMMSXMMSMXSMXMSSMSSSMMSMAMXMXSMMMMAXAMXSASXSSMMSSMXAMXMSAMXMMXAXXXSAMXXXXXMMXSXMXXSMASAMXMXAXXMAS"))
    print(exercise_01("input.txt"))


if __name__ == "__main__":
    main()