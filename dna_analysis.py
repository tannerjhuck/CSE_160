# Name: Tanner Huck
# CSE 160
# Homework 2: DNA analysis

# This program reads in DNA sequencer output and computes statistics, such as
# the GC content, AT content, nucleotide counts, etc.  Run it from the command
# line like this:
#   python dna_analysis.py myfile.fastq
#
# For teaching purposes, a few more comments than normal have been added in
# to explain in detail what some Python constructs are doing.

# The sys module supports reading files, command-line arguments, etc.
import sys


# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    """
    dna_filename - the name of a file in expected file format
    Expected file format is: Starting with the second line of the file,
    every fourth line contains nucleotides.
    The function will read in all lines from the file containing nucleotides,
    concatenate them all into a single string, and return that string.
    """

    # YOU DO NOT NEED TO MODIFY THIS FUNCTION.

    # Creates a file object from which data can be read.
    inputfile = open(dna_filename)

    # String containing all nucleotides that have been read from the file so
    # far.
    seq = ""

    # The current line number (= the number of lines read so far).
    line_num = 0

    for line in inputfile:
        line_num = line_num + 1
        # if we are on the 2nd, 6th, 10th line...
        if line_num % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line
    # close file
    inputfile.close()
    return seq


# Function to return GC Classification
def classify(gc_content):
    if gc_content < 0.37:  # if gc_content is less that 37 it is low class
        classification = "low"
    elif gc_content > 0.55:
        # if gc_content is more that 55 it is low class
        classification = "high"
    else:
        # if gc_content is not less than 37 or higher than 55
        classification = "moderate"  # it is moderate class
    return classification


###########################################################################
# Main program begins here
#

# Check if the user provided an argument
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this "
          "program.")
    sys.exit(2)

# Save the 1st argument provided by the user, as a string.
# Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
file_name = sys.argv[1]

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(file_name)

###
# Compute statistics
###

# YOUR CODE GOES BELOW THIS POINT

# Total nucleotides seen so far.
total_count = 0

# Variables to count number of G,C,A,T nucleotides
g_count = 0
c_count = 0
a_count = 0
t_count = 0

# For loop that will go through all the nucleotides
for base in nucleotides:
    total_count = total_count + 1

    # If the nucleoutide is a C, add one to the gc and c counts
    if base == 'C':
        c_count = c_count + 1
    # If the nucleoutide is a G, add one to the gc and g counts
    elif base == 'G':
        g_count = g_count + 1
    # If the nucleoutide is a A, add one to the a and a counts
    elif base == 'A':
        a_count = a_count + 1
    # If the nucleoutide is a T, add one to the t and a counts
    elif base == 'T':
        t_count = t_count + 1

# determines the GT and AT count and content
gc_count = g_count + c_count
at_count = a_count + t_count
# calculates the sum of G,C,A,T counts
g_c_a_t_count_sum = g_count + c_count + a_count + t_count

# calculates the gc and at content
gc_content = gc_count / g_c_a_t_count_sum
at_content = at_count / g_c_a_t_count_sum
# Printing the Agc and at content
print('GC-content:', gc_content)
print('AT-content:', at_content)

# Printing out the different nucleotide counts
print('G count:', g_count)
print('C count:', c_count)
print('A count:', a_count)
print('T count:', t_count)

# prints the sum of G,C,A,T counts
print('Sum of G+C+A+T counts:', g_c_a_t_count_sum)

# prints the total count
print('Total count:', total_count)

# calculates and prints the length of the nucleotides string variable
print('Length of nucleotides:', len(nucleotides))

# Calcculates and prints the AT/GC ratio
at_gc_ratio = at_count / gc_count
print('AT/GC Ratio:', at_gc_ratio)

# Printing out the classification
print("GC Classification:", classify(gc_content), "GC content")

# You can add more assertions here to check properties that you think
# should be true about your results. If the condition listed is false,
# then the given message will be printed.
assert total_count == len(nucleotides), "total_count != length of nucleotides"
