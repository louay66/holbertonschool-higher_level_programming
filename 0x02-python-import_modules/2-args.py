#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0 arguments.")
    elif i == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(i - 1))
        for a in range(1, i):
            print("{:d}: {:s}".format(a, sys.argv[a]))
