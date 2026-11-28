#!/usr/bin/env python3
"""
Two-pass Hack assembler for the Nand2Tetris course.

Usage:
    python3 assembler.py Program.asm [Program.hack]
"""

import argparse
import sys
from pathlib import Path


PREDEFINED_SYMBOLS = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4,
    "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9,
    "R10": 10, "R11": 11, "R12": 12, "R13": 13,
    "R14": 14, "R15": 15,
    "SCREEN": 16384, "KBD": 24576,
}

DEST_TO_BITS = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111",
}

COMP_TO_BITS = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "!D": "0001101",
    "!A": "0110001", "-D": "0001111", "-A": "0110011",
    "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
    "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    "M": "1110000", "!M": "1110001", "-M": "1110011",
    "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
    "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
    "D|M": "1010101",
}

JUMP_TO_BITS = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
}


def clean_source(lines):
    cleaned = []
    for source_line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.split("//", 1)[0].strip()
        if line:
            cleaned.append((source_line_number, line))
    return cleaned


def first_pass(cleaned_lines):
    symbols = dict(PREDEFINED_SYMBOLS)
    instructions = []
    rom_address = 0

    for source_line_number, line in cleaned_lines:
        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1].strip()
            if not label:
                raise ValueError(source_line_number, "invalid instruction")
            if label in symbols:
                raise ValueError(source_line_number, "invalid instruction")
            symbols[label] = rom_address
        else:
            instructions.append((source_line_number, line))
            rom_address += 1

    return symbols, instructions


def parse_c_instruction(line):
    if "=" in line:
        dest, expression = line.split("=", 1)
        dest = dest.strip()
    else:
        dest, expression = "", line

    if ";" in expression:
        comp, jump = expression.split(";", 1)
        comp = comp.strip()
        jump = jump.strip()
    else:
        comp = expression.strip()
        jump = ""

    if dest not in DEST_TO_BITS:
        raise KeyError
    if comp not in COMP_TO_BITS:
        raise KeyError
    if jump not in JUMP_TO_BITS:
        raise KeyError

    return "111" + COMP_TO_BITS[comp] + DEST_TO_BITS[dest] + JUMP_TO_BITS[jump]


def assemble(input_path):
    lines = input_path.read_text(encoding="utf-8").splitlines()
    cleaned = clean_source(lines)
    symbols, instructions = first_pass(cleaned)

    next_variable_address = 16
    binary_lines = []

    for source_line_number, line in instructions:
        if line.startswith("("):
            continue

        if line.startswith("@"):
            token = line[1:].strip()
            if not token:
                raise ValueError(source_line_number, "invalid instruction")

            if token.isdigit():
                address = int(token, 10)
                if address > 32767:
                    raise ValueError(source_line_number, "invalid instruction")
            else:
                if token not in symbols:
                    symbols[token] = next_variable_address
                    next_variable_address += 1
                address = symbols[token]

            binary_lines.append(format(address, "016b"))
        else:
            try:
                binary_lines.append(parse_c_instruction(line))
            except (KeyError, ValueError):
                raise ValueError(source_line_number, "invalid instruction")

    return binary_lines


def main():
    parser = argparse.ArgumentParser(description="Assemble a Hack .asm file")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", nargs="?", type=Path)
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"Line 1: input file not found: {args.input}", file=sys.stderr)
        return 1

    output_path = args.output or args.input.with_suffix(".hack")

    try:
        binary_lines = assemble(args.input)
    except ValueError as error:
        line_number, message = error.args
        print(f"Line {line_number}: {message}", file=sys.stderr)
        return 1

    output_path.write_text("\n".join(binary_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
