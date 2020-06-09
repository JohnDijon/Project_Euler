with open('other_files/13.txt') as digit_file:
   digit_list = []
   for line in digit_file:
        digit_list.append(int(line))


def problem_solve():
    digit_sum = 0
    for digit_line in digit_list:
        digit_sum += digit_line
    
    return str(digit_sum)[:10]

#def problem_solve():
#    """ or shorter using sum() """
#    return str(sum(digit_list))[:10]

if __name__ == "__main__":
    print(problem_solve())
    
