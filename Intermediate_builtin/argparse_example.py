''' Argparse is a parser for command-line options, arguments and subcommands. 
Argparse is helpful when you want to make a program that will interact directly into 
the command line and not using the python Idle. '''

# First is we import argparse and sys.
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,   # Be used to 'no spaces' when typing equal sign
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


# Using this simple calculator code

'''
def calc(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y
'''

# We will modify this code to make it work with Argparse.

def calc(args):
	if args.operation == 'add':
		return args.x + args.y
	elif args.operation == 'sub':
		return args.x - args.y
	elif args.operation == 'mul':
		return args.x * args.y
	elif args.operation == 'div':
		return args.x / args.y

if __name__ == '__main__':
	main()

# To get this thing work in a command line
# python3 Argparse.py --x = 5 --y = 5 --operation = mul

# Or to get all the functionalities, use help
# python Arparse.py -h