#!/usr/bin/env python3
#
# Brainfuck Interpreter
# Copyright 2011 Sebastian Kaspari
#
# Usage: ./brainfuck.py [FILE]

import sys
import getch

debug = False

def execute(filename):

    f = open(filename, "r")
    raw_code = f.read()
    f.close()

    output = evaluate(raw_code,raw_input="Foobarbaz",max_ticks=10000)
    print("[{}]".format(output))


def evaluate(code,raw_input=None,max_ticks = None):

    code_filter = cleanup(list(code))
    code = [c for c in code_filter]

    try:
        bracemap = buildbracemap(code)
    except IndexError:
        raise Exception("Bad code")

    input = None
    if raw_input is not None:
        input = list(raw_input)

    input_idx = 0
    output_buf = []

    cells, codeptr, cellptr = [0], 0, 0

    tick_counter = 0
    while codeptr < len(code):

        if max_ticks is not None and tick_counter > max_ticks:
            raise Exception("Long runner")

        command = code[codeptr]

        if command == ">":
            cellptr += 1

        if cellptr == len(cells):
            cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0:
            codeptr = bracemap[codeptr]

        if command == "]" and cells[cellptr] != 0:
            codeptr = bracemap[codeptr]

        if command == ".":
            output_buf.append(chr(cells[cellptr]))
            sys.stdout.write(chr(cells[cellptr]))
            sys.stdout.flush()

        if command == ",":
            if input is None:
                raise Exception("Not expecting input")
            else:
                if input_idx < len(input):
                    cells[cellptr] = input[input_idx]
                    input_idx += 1
                else:
                    raise Exception("Input not long enough")
      
        codeptr += 1
        tick_counter += 1

    return "".join(output_buf)


def cleanup(code):
    return filter(lambda x: x in list('.,[]<>+-'), code)


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[":
            temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap


def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__":
    main()
