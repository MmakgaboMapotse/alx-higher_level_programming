#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    return add(a, b) + sum(range(4, 6)) if a < b else sub(a, b)
