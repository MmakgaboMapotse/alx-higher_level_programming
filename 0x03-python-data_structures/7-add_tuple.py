#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = tuple_a + (0, 0)

    b = tuple_b + (0, 0)
    result = (a[0] + b[0], a[1] + b[1])

    return result

tuple1 = (1, 2)
tuple2 = (3, 4)
result_tuple = add_tuple(tuple1, tuple2)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Result:", result_tuple)

