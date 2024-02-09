"""Reads file and retrieves statistics"""
import sys
import time

start_time = time.time()
if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    sys.exit()
INPUT_FILE = str(sys.argv[1])

def check_numeric(string):
    """Function identifying and transforming numeric"""
    try:
        return float(string)
    except ValueError:
        return None

with open(INPUT_FILE, 'r') as f:
    llist= f.readlines()

num_list =  [check_numeric(line) for line in llist if check_numeric(line) is not None]



def get_statistics(input_list):
    """Calculates Statistics"""
    sorted_input = sorted(input_list)
    input_length = len(sorted_input)

    mean = sum(sorted_input)/input_length

    middle_idx = (input_length - 1) //2
    median = sorted_input[middle_idx]
    if input_length % 2 == 0:
        middle_number_1 = sorted_input[middle_idx]
        middle_number_2 = sorted_input[middle_idx +1]
        median = (middle_number_1 +middle_number_2)/2

    number_counts = {x: sorted_input.count(x) for x in set(sorted_input)}
    mode = max(number_counts.keys(), key=lambda unique_number: number_counts[unique_number])

    sample_variance=sum([(number-mean)**2 / (input_length - 1) for number in sorted_input])

    sample_standard_deviation = sample_variance**0.5


    return {
        "COUNT": input_length,
        "MEAN": mean,
        "MEDIAN": median,
        "MODE": mode,
        "SD": sample_standard_deviation,
        "VARIANCE": sample_variance,
    }

stats_output= get_statistics(num_list)
time_elapsed =time.time() - start_time
print("--- %s seconds elapsed" % time_elapsed)

with open('StatisticsResults.txt', 'a') as f:
    f.write(INPUT_FILE + ' results:\n')
    for key, value in stats_output.items():
        f.write('%s:%s\n' % (key, value))
    f.write('Execution time:' + str(time_elapsed) + ' seconds\n')
    f.write('--------------------------------------------------\n')
    