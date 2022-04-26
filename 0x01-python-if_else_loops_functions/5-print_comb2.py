#!/usr/bin/python3
for a in range(0, 100):
    if a < 99:
        print("{:0>2d}".format(a), end=", ")
    else:
        print(f"{a}")
