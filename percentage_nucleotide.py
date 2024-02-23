import sys, re
from argparse import ArgumentParser

# Set up the parser!
parser = ArgumentParser(description=' This module classify a sequence as either DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# Check the length of the input sequence
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Set args as the output of the parser script
args = parser.parse_args()

# Convert the sequence to uppercase in order to make it case insensitive 
args.seq = args.seq.upper()

if re.search('^[ACGTU]+$', args.seq):
    if re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence is DNA')
else:
    print ('The sequence is neither DNA nor RNA')
    sys.exit(1) 


# Set up counter variables
counter = {}

sequence_length = len(args.seq)

# Set up loop to check the letters and increase count per letter
for letter in args.seq:
	if letter in counter:
		counter[letter] += 1
	else:
		counter[letter] = 1

# Print at first place the type of input sequence {either DNA or RNA}
print('The sequence is DNA' if "T" in args.seq else 'The sequence is RNA' if "U" in args.seq else 'The sequence is DNA or RNA')

# Print the counts of nucleotides
for letter, counter in counter.items():
	print(f"%{letter}: {counter / sequence_length * 100:.2f}%")

