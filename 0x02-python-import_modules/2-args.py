#!/usr/bin/python3
from sys import argv

def main():
    num_args = len(argv) - 1

    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args), end="")
    print(":", end="\n" if num_args > 0 else ".")
    
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    main()

