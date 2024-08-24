"""
This script demonstrates a basic exercise in greeting a user.

Exercise Description:
1. Print "Hello, world!" on the screen.
2. Prompt the user to enter their name.
3. Greet the user by name with "Hello, [name]".

Example output with the name "Alice":

Hello, world!
What is your name?
Alice
Hello, Alice

Prerequisite concepts: print(), strings, string concatenation

Solution Below
"""

print("Hello, world!")
user_name = input("What is your name? \n")
print(f"Hello, {user_name}")
