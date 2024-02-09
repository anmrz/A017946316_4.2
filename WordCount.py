"""Counts words in text."""
import sys
import time
start_time = time.time()

if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    sys.exit()
INPUT_FILE = str(sys.argv[1])

# Create an empty dictionary
text_dict = dict()

# Loop through each line of the file
with open(INPUT_FILE, 'r') as text:
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert chars to lowercase
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over words in line
        for word in words:
            if word in text_dict:
                text_dict[word] = text_dict[word] + 1
            else:
                text_dict[word] = 1

time_elapsed =time.time() - start_time
print("--- %s seconds elapsed" % time_elapsed)

with open('WordCountResults.txt', 'a') as f:
    f.write(INPUT_FILE + ' results:\n')
    for key, value in text_dict.items():
        f.write('%s:%s\n' % (key, value))
    f.write('Execution time:' + str(time_elapsed) + ' seconds\n')
    f.write('--------------------------------------------------\n')
