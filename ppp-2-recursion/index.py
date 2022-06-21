"""
Write a program that takes a positive number (n) as an arg and prints the numbers from (n) to 0
"""
def return_to_zero(n):
    for i in range(n, -1, -1): print(i);

def return_to_zero_rec(n):
    print('Recursive=>',n);
    return 0 if n == 0 else return_to_zero_rec(n - 1);

return_to_zero(4);
return_to_zero_rec(4);


"""
Write a program that takes a positive number (n) as an arg and prints the numbers from 0 to (n)
"""

def go_to_n(n):
    for i in range(0, n + 1, 1): print(i);

def go_to_n_rec(n, curr = 0):
    print('Recursive=>',curr);
    return 0 if n <= curr else go_to_n_rec(n, curr + 1);

go_to_n(5);
go_to_n_rec(7);


"""
Write a program that returns the nth elements in the fivonacci sequence
"""

def fib_rec(n, curr_n = 2, last = 0, now = 0):
    if n == 0: return; # They want 0
    print('Fib->', last + now);
    if n == 1: return; # We printed first one, exit
    if last + now == 0: print('Fib->', 1);
    # We've printed two first call, curr_n should start at 2
    return 0 if n <= curr_n else fib_rec(n, curr_n + 1, 1 if now == 0 else now, last + now);

fib_rec(18);


"""
Write a program that calculates the value of 'a' to the power of 'b'
"""

pow_rec = lambda a, b: a * pow_rec(a, b - 1) if b > 1 else a
print(pow_rec(2,3))

"""
Write a program that determines if a string is a palindrome
"""

def is_pal(str):
    start = 0;
    end = len(str) - 1;
    while start < end:
        if str[start] != str[end]: return False;
    return True;


def is_pal_rec(str, index = 0):
    if len(str) / 2 <= index: return True;
    if str[index] != str[-index-1]: return False;
    return is_pal_rec(str, index + 1);

print('kayak=>',is_pal_rec('kayak'));
print('lololoaaaololol=>', is_pal_rec('lololoaaaololol'));
print('console=>', is_pal_rec('console'))


def find_common_divisors(num1, num2):

    def find_all_divisors(num, n, list):
        if (num % n == 0): list.append(n);
        return list if num <= n else find_all_divisors(num, n + 1, list)

    def find_highest(arr1, arr2):
        hash = sorted({*arr1, *arr2}, key=lambda item: -item);
        for i in hash:
            if i in arr1 and i in arr2: return i
        return -1 # We should never get here. Everything should share 1

    return find_highest(find_all_divisors(num1, 1, []), find_all_divisors(num2, 1, []))



print('Result=>', find_common_divisors(645, 165));

# Code from Solution
gcd = lambda x, y: x if y == 0 else gcd(y, x % y)
print(gcd(165, 645));