import os

# Define the maximum number of words per file
MAX_WORDS_PER_FILE = 1000000

# Open the input file for reading
with open('wordlist.txt', 'r') as input_file:
    # Initialize the word counter and file counter
    word_count = 0
    file_count = 1
    # Open the first output file for writing
    output_file = open(f'output_{file_count}.txt', 'w')
    # Loop through the lines in the input file
    for line in input_file:
        # Write the line to the current output file
        output_file.write(line)
        # Increment the word counter
        word_count += 1
        # If the maximum number of words per file has been reached,
        # close the current output file and open a new one
        if word_count == MAX_WORDS_PER_FILE:
            output_file.close()
            file_count += 1
            output_file = open(f'output_{file_count}.txt', 'w')
            # Reset the word counter
            word_count = 0
    # Close the final output file
    output_file.close()

# Print the number of output files created
num_files = len([name for name in os.listdir('.') if os.path.isfile(name) and name.startswith('output_')])
print(f'{num_files} output files created.')
