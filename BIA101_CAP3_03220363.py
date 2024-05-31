################################
#https://github.com/sanjalapradhan/03220363_BIA101_CAP3
# sanjala Pradhan
# BBI "A"
# 03230363
################################
# REFERENCES
# https://youtu.be/0yIFEJ879lw?si=USq7yD2XPMWaACh4
# https://youtu.be/Uh2ebFW8OYM?si=IMGxkkwb2fSwTMFl
################################
# SOLUTION
# Solution Score: 490742
################################

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def extract_two_digit_number(line):
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            first_digit = char
            break

    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break

    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0

def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        two_digit_number = extract_two_digit_number(line)
        total_sum += two_digit_number
    return total_sum

def print_solution(file_name, total_sum):
    print(f"The total sum of from the given input file {file_name} is {total_sum}")

if __name__ == "__main__":
    input_file = '363.txt'
    lines = read_input(input_file)
    total_sum = calculate_sum(lines)
    print_solution(input_file, total_sum)
