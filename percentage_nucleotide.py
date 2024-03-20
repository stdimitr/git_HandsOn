import sys, re
from argparse import ArgumentParser

# Define the parser
parser = ArgumentParser(description=' This module classify a sequence as either DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# Check the length of the input sequence
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Set args as the output of the parser script
args = parser.parse_args()

# Convert the input sequence to uppercase in order to make it case insensitive 
args.seq = args.seq.upper()

if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq): #Only T is present (NOT U is present)
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq): #Only U is present (NOT T is present)
        print ('The sequence is RNA')
    elif re.search('T', args.seq) and re.search('U', args.seq): # If we type a wrong sequence that includes both T & U
        print ('The sequence cannot contain both T and U')
    else: # If the sequence contains ONLY ACG than we cannot decide if it is DNA or RNA sequence
        print ('The sequence can be DNA or RNA')
else: # neither DNA or RNA
    print ('The sequence is neither DNA nor RNA')
    sys.exit(1) 


# Define counter variables
counter = {}

sequence_length = len(args.seq)

# Set up loop to check the letters and increase count per letter
for letter in args.seq:
	if letter in counter:
		counter[letter] += 1
	else:
		counter[letter] = 1


# Print the counts of nucleotides
for letter, counter in counter.items():
	print(f"%{letter}: {counter / sequence_length * 100:.2f}%")

#Nice code :)
