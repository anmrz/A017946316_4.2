# with open('TC4.txt', 'r') as f:
#     llist= f.readlines()
# input_list =  [int(line) for line in llist]

def binary_convert(decimal_numb):
    aux_string = ''

    while decimal_numb:
        resid = decimal_numb % 2
        decimal_numb = int(decimal_numb / 2)
        aux_string = str(resid) + aux_string
        # aux_stack.append(resid)
        
    return aux_string

# print(binary_convert(13))

# def num_concat(num1, num2):
#   return int("{}{}".format(num1, num2))

def hexa_convert(decimal_numb):
    aux_string = str(int(decimal_numb)) + "°"
    decimal_part = decimal_numb - int(decimal_numb)

    while decimal_part>0:
        hexa_prod = decimal_part * 60
        step_result = int(hexa_prod)
        decimal_part = hexa_prod - step_result
        aux_string = aux_string + ' " ' + str(step_result)
        print(decimal_part) 
    return aux_string

print(hexa_convert(121))