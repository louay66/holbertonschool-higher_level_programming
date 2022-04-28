#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i  = 0  
    if len(argv) > 2:
        for c in range(1, len(argv)):
            i += int(argv[c])

    print(f"{i}")

