#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif op == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif op == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif op == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
