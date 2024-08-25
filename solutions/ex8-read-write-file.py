"""
You will write three functions for this exercise. First, write a write_to_file() function with two parameters for the filename of the file and the text to write into the file. Second, write an append_to_file() function, which is identical to write_to_file() except that the file opens in append mode instead of write mode. Finally, write a read_from_file() function with one parameter for the filename to open. This function returns the full text contents of the file as a string.

These Python instructions should generate the file and the assert statement checks that the content is correct:

write_to_file('greet.txt', 'Hello!\n')

append_to_file('greet.txt', 'Goodbye!\n')

assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'

This code writes the text 'Hello!\n' and 'Goodbye!\n' to a file named greet.txt, then reads in this file’s content to verify it is correct. You can delete the greet.txt file after running these instructions program.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: text file reading and writing
"""


def write_to_file(filename, text):

    # Open the file in write mode:

    with open(filename, 'w') as file_object:

        # Write the text to the file:

        file_object.write(text)


def append_to_file(filename, text):

    # Open the file in append mode:

    with open(filename, 'a') as file_object:

        # Write the text to the end of the file:

        file_object.write(text)


def read_from_file(filename):

    # Open the file in read mode:

    with open(filename) as file_object:

        # Read all of the text in the file and return it as a string:

        return file_object.read()


write_to_file('greet.txt', 'Hello!\n')

append_to_file('greet.txt', 'Goodbye!\n')

assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'
