"""Transforms numbers into binary and hexagesimal."""
import sys
import time
start_time = time.time()

if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    sys.exit()
INPUT_FILE = str(sys.argv[1])


with open(INPUT_FILE , 'r') as f:
    llist= f.readlines()

def check_numeric(string):
    """Function identifying and transforming numeric"""
    try:
        return int(string)
    except ValueError:
        return None

input_list =  [check_numeric(line) for line in llist]

def extract_sign(decimal_numb):
    """Catches sign."""
    if decimal_numb <0:
        return -1
    return 1

def uns_to_bi(decimal_numb, aux_stack):
    """Transforms unsigned number into binary."""
    if decimal_numb > 0:
        aux_stack.append(decimal_numb%2)
        uns_to_bi(decimal_numb//2, aux_stack)
    return aux_stack

def bin_incr_unit(binary_list):
    """Adds 1 to a binary number"""
    for i in range (len(binary_list)-1, -1, -1):
        if binary_list[i] == 0:
            binary_list[i] = 1
            break
        binary_list[i] = 0
    return binary_list

def sign_to_bi(aux_stack):
    """Transforms signed number into binary."""
    count = 16 - len(aux_stack)
    padding = [0]*count
    padded_list = padding + aux_stack
    aux_stack = [1 if i== 0 else 0 for i in padded_list]
    bin_incr_unit(aux_stack)
    return aux_stack

def dec_to_bin(decimal_numb):
    """Transforms number into binary."""
    if decimal_numb==0:
        return '0'
    sign_unit = extract_sign(decimal_numb)
    uns_numb =  sign_unit * decimal_numb
    aux_stack =[]
    uns_to_bi(uns_numb, aux_stack)
    aux_stack.reverse()

    if sign_unit == -1:
        aux_stack = sign_to_bi(aux_stack)

    bin_rep = ''.join([str(l) for l in aux_stack])

    return bin_rep

def bin_to_hexa(numb):
    """Transforms binary into hexagesimal."""
    num = int(numb, 2)
    hex_num = format(num, 'X')
    return hex_num


converted = [[str(numb), dec_to_bin(numb), bin_to_hexa(dec_to_bin(numb))]
            if numb is not None else [str(numb), '#VALUE!', '#VALUE!']
            for numb in input_list
            ]
            
time_elapsed =time.time() - start_time
print("--- %s seconds elapsed" % time_elapsed)

with open('ConvertionResults.txt', 'a') as f:
    f.write(INPUT_FILE + ' results:\n')
    f.write('INPUT_NUMB     BIN     HEX\n')

    for line in converted:
        f.write('       '.join(line) + '\n')
    f.write('Execution time:' + str(time_elapsed) + ' seconds\n')
    f.write('--------------------------------------------------\n')
    