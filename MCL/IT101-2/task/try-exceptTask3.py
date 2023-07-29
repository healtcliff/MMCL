'''
a "SyntaxError" occurs because there is a missing closing parenthesis after the string 
"Hello, World!". The except block catches the exception and prints an error message.
try:
    print("Hello, World!"
except SyntaxError:
    print("Error: Syntax error!")
'''
'''
a "TypeError" occurs because we are trying to concatenate a string ("Hello") with an integer (10), 
which is not allowed. The except block catches the exception and prints an error message.
try:
    result = "Hello" + 10
except TypeError:
    print("Error: Incompatible data types!")
'''
'''
a "NameError" occurs because the variable y has not been defined before using it in the expression. 
The except block catches the exception and prints an error message.
try:
    x = y + 5
except NameError:
    print("Error: Variable not found!")
'''

'''
an "IndexError" occurs because we are trying to access the element at index 3 in a list that only has indices 0, 1, and 2.
The except block catches the exception and prints an error message.
try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError:
    print("Error: Index out of range!")
'''

'''
a "KeyError" is raised because the key "address" does not exist in the dictionary. 
The except block catches the exception and prints an error message.
try:
    my_dict = {"name": "John", "age": 30}
    print(my_dict["address"])
except KeyError:
    print("Error: Key not found!")
'''

'''
a "ValueError" occurs because the string "abc" cannot be converted to an integer. 
The except block catches the exception and prints an error message.
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid value!")
'''

'''
an "AttributeError" occurs because we are trying to call the non-existent method nonexistent_method() on the list object my_list. 
As a result, the except block is executed, and the error message "Error: Attribute not found!" is printed..
try:
    my_list = [1, 2, 3]
    my_list.sort(reverse=True)
except AttributeError:
    print("Error: Attribute not found!")
'''

'''
an "IOError" occurs because the file named "nonexistent.txt" does not exist or cannot be opened.
The except block catches the exception and prints an error message.
try:
    file = open("nonexistent.txt", "r")
except IOError:
    print("Error: File not found or cannot be opened!")
'''

'''
a "ZeroDivisionError" occurs because division by zero is undefined. 
The except block catches the exception and prints an error message.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
'''

'''
an ImportError occurs because the module named "nonexistent_module" does not exist. 
The except block catches the exception and prints an error message.
try:
    import nonexistent_module
except ImportError:
    print("Error: Module not found!")
'''