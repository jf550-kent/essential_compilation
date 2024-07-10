# This python program allows you to bake the number of cakes you specific
def bake_cake(num: int):
    for i in range(1, num+1):
        print("bake cake" + str(i))

bake_cake("Hello")    

# ------------------------ #
# From words to AST
# ------------------------ #
# Here we are using concrete syntax, to represent a program that bakes cakes.
# In this context, concrete syntax is actual words and letter you type with your keyboard.

# At the lowest level, the cpu of the computer only understand 0 and 1. 
# Therefore, in order for our cake baking programs works, we need to transform it to the lowest level. 
# This is the compiler's job to transform it.

# First, we need to transform the concrete syntax into abstract syntax tree. Representing our program in 
# abstract syntax tree allows the compiler perform various operations more efficiently. This process is called parsing.

# ------------------------ #
# Grammars
# ------------------------ #
"""
Grammars in just the rules how you can write your program. For instance, to write
a function in python you need to write it in this way.

def function_name():
    print("this is a function")

Defining the grammar of your language, allows you to build the AST
"""

# ------------------------ #
# Abstract syntax tree
# ------------------------ #
"""
Abstract syntax tree allows compiler to easily look at the each part of the tree to identify 
the language feature.

get_number() + (-8)

          +
    /           \
get_number()     -
                  \
                  8
"""