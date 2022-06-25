unordered_list_of_tuple = [
    ('English', 88),
    ('Science', 90),
    ('Maths', 97),
    ('Social Studies', 82)
]

"""
Write a program that sorts these based on the second item in the tuple. Low -> High
"""

sorted_list_tuples = sorted(unordered_list_of_tuple, key = lambda item: item[1])
print(f"Unsorted list: {unordered_list_of_tuple}")
print(f"Sorted list: {sorted_list_tuples}")




uncubed_list = [3, 6, 9, 2]

"""
Write a program that cubes each item in the list. Use Lambda function(s)
"""

cubed_list = [*map(lambda x: x**2, uncubed_list)]
print(f"Uncubed list: {uncubed_list}")
print(f"Cubed list: {cubed_list}")



even_odd_list = [3, 6, 9, 2]
"""
Write a program that determines if each of the items is even or odd. Replace the item with 'Even' or 'Odd'
"""

true_false_list = list(map(lambda item: item % 2 == 0, even_odd_list))
print(f"Even/odd list: {even_odd_list}")
print(f"True false list: {true_false_list}")


"""
Use list comprehension to create a list from 1 to 100
"""
# big_list = list(range(1, 101))
big_list = [i for i in range(1, 101)]
print(big_list)


"""
Use dictionary comprehension to count each letter in a string
"""
input_string = "The quick brown fox jumped over the fence."
dict_word_count = {word: len(word) for word in input_string.split()}
print(f"Input string: {input_string}")
print(f"Dictionary letter counter: {dict_word_count}")
