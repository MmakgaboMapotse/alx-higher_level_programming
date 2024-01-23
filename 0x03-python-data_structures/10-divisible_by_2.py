#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [False if num % 2 else True for num in my_list]

original_list = [1, 2, 3, 4, 5]
result_list = divisible_by_2(original_list)
print("Original List:", original_list)
print("Result List:", result_list)

