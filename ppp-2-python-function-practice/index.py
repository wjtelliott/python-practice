"""
William E - 6/20/2022@11:29PM
"""
print('\n\n\n')

"""
max_num - find the maximum of up to at least three numbers
"""
max_num = lambda *ints: sorted([*ints], key=lambda item: -item)[0]
print('max_num(3,4,1,2,2,3,1)=>', max_num(3, 4, 1, 2, 2, 3, 1))
# expected output: 4

"""
mult_list - multiply all numbers in a list
"""
mult_list = lambda num_list: __import__('functools').reduce(lambda total, current: total * current, num_list)
print('mult_list([7,7,2])=>', mult_list([7, 7, 2]))
# expected output: 98

"""
rev_string - reverse a string
"""
rev_string = lambda str: str[::-1]
print('rev_string(\'Reverse!\')=>', rev_string('Reverse!')) # Expected output: !esreveR

"""
num_within - receives a number, beginning of range, end of range and
    returns bool if the number falls within the range given
"""
num_within = lambda num, min, max: num in range(min, max)
print('num_within(10,2,5)=>', num_within(10,2,5)) # Expected output: false

"""
pascal - prints out the first n rows of Pascal's triangle
"""
print('\n\nPascal\'s triangle using recursion:')
# a poor try at recursive pascal.
# need to figure out how to merge the helper func
# Maybe the two-way recursive funcs like we saw in class today?
def pas_rec(n, depth = 0, current_row = [1]):
    if n < 1 or depth >= n: return
    # Helper to create new rows
    def create_new_row(prev_row):
        new_row = []
        for i in range(0, len(prev_row) + 1):
            new_row.append(1 if i == len(prev_row) or i == 0 else prev_row[i] + prev_row[i-1])
        return new_row
    # We can use this to add some spaces to the beginning and make it look cleaner.
    # end='' to make sure we don't add a new line
    print(' '*(n-depth), end='');
    print(" ".join(str(i) for i in current_row))
    pas_rec(n, depth + 1, create_new_row(current_row))
pas_rec(5);


print('\n\nPascal\'s triangle without using rec funcs:')
# Without rec
def pascal(n):
    if n < 1: return

    # Helper to create new rows
    def create_new_row(prev_row):
        new_row = []
        for i in range(0, len(prev_row) + 1):
            new_row.append(1 if i == len(prev_row) or i == 0 else prev_row[i] + prev_row[i-1])
        return new_row
    
    # all rows
    current_row = [1]
    for _ in range(0, n):
        print(" ".join(str(i) for i in current_row))
        current_row = create_new_row(current_row)
    


pascal(12)
"""
expected output example(5):
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""