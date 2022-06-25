import re
class FileManipulator:
    def __init__(self, file) -> None:
        
        check_valid_file_path = lambda str: re.match(r'^[a-zA-Z0-9\-\_]+\.txt$', str) != None

        # Not sure why this should be in constructor

        file_path = file
        while check_valid_file_path(file_path):
            file_path = str(input('Enter a file name:'))
            try:
                my_file = open(file_path, 'r')
            except FileNotFoundError as f:
                print(f"Could not find file! {f}")
                # Must set file_path to a string that will cause check_valid_file to be True to loop
                file_path = "none.txt"
            else:
                file_contents = my_file.readlines()
                print(file_contents)

                reversed_file = open('reversed_' + file_path, 'w')
                reversed_file.write("\n".join(self.reverse(file_contents)))

                upper_file = open('upper_' + file_path, 'w')
                upper_file.write("\n".join(self.upper(file_contents)))

                my_file.close()
                reversed_file.close()
                upper_file.close()

                file_path = 'exit'

    reverse = lambda _, in_list: [item[::-1] for item in in_list]
    upper = lambda _, in_list: [item.upper() for item in in_list]

f = FileManipulator("none.txt")
