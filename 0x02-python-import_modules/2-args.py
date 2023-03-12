#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_argv = len(sys.argv) - 1

    if num_argv == 0:
        print("{:d} arguments".format(num_argv))
    elif num_argv == 1:
        print("{:d} argument".format(num_argv))
    else:
        print("{:d} arguments".format(num_argv))
    for num_argv in range(0, num_argv):
        print("{:d}: {:s}".format(num_argv + 1, sys.argv[num_argv + 1]))
