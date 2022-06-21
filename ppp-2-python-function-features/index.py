"""
Complete the following functions:
    arb_args - takes in any number of arguments and prints them one at a time
    inner_func - takes in two ints, two nested functions should perform separate,
        distinct math operations using the ints. The result of both nested functions should then be added and printed
    lunch_lady - takes in two strings, a students name and their lunch preference. The function should print both
        strings. If a lunch preference is not given, mystery meat should be printed instead
    sum_n_product - accepts two ints and returns both the sum and product
    alias_arb_args - should be arb_args but assigned as an alias. remember variables can hold
        functions in python just like JS
    arb_mean - accepts any number of ints and prints their average
    arb_longest_string - accepts any number of string and returns the longest one
"""

def arb_args(*args):
    for i in args: print(i);

def inner_func(num1, num2):
    add = lambda a, b: a + b;
    subtract = lambda a, b: a - b;
    return add(num1, num2), subtract(num1, num2);

lunch_lady = lambda name, pref = 'Mystery Meat': print("{s_name}\'s preference is: {food}".format(s_name = name, food = pref));

def sum_n_product(num1, num2):
    return num1+num2, num1*num2;

# OR alias_arb_args = arb_args;
alias_arb_args = lambda *args: arb_args(*args);

arb_mean = lambda *arr: __import__('functools').reduce(lambda a, b: a + b, [*arr]) / len([*arr]);

arb_longest_string = lambda *strings: sorted([*strings], key= lambda item: len(item))[-1];



#Lets test these funcs!

arb_args('string', 'second', 'third', 'last');

print(inner_func(1, 2));

lunch_lady('Isiah', 'Pizza');
lunch_lady('Tom');

print(sum_n_product(5, 9));

alias_arb_args('alias', 'second', 'last');

print(arb_mean(5, 5, 7, 3, 2, 9, 3, 5, 1));

print(arb_longest_string('string', 'asd', 'a', 'longgggggg', 'not long'));
