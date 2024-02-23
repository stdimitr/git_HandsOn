
#!/usrbin//env python3

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args() 

args.seq= args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq): #Only T is present
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq): #Only U is present
        print ('The sequence is RNA')
    elif re.search('T', args.seq) and re.search('U', args.seq): # For a wrong typing where both T & U are present !
        print ('ERROR: The sequence contains both T and U')
    else: # We cannot decide if it is DNA or RNA - both are possible - If the sequence contains ONLY AG
        print ('The sequence can be DNA or RNA')
else: # neither DNA or RNA
    print ('The sequence is neither DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("MOTIF FOUND")

    else:
        print("MOTIF NOT FOUND")

