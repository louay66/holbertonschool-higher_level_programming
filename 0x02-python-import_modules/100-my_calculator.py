#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        opprtor = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if opprtor == '+':
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res))
        elif opprtor == '-':
            res = sub(a, b)
            print("{} - {} = {}".format(a, b, res))
        elif opprtor == '*':
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res))
        elif opprtor == '/':
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
