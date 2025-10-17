# ---------------------------------------------
# Chapter 2 Practice Script
# Topics: Literals, Constants, Keywords, Identifiers, Variables, Comments
# ---------------------------------------------

# ----------------------
# 1. Comments
# ----------------------
# This is a single-line comment
"""
This is a multi-line comment
used for documentation purpose
"""

# ----------------------
# 2. Literals
# ----------------------
int_literal = 10
float_literal = 3.14
string_literal = "Hello, Cloud!"
bool_literal = True
list_literal = [1, 2, 3]

print("Integer Literal:", int_literal)
print("Float Literal:", float_literal)
print("String Literal:", string_literal)
print("Boolean Literal:", bool_literal)
print("List Literal:", list_literal)

# ----------------------
# 3. Constants (by convention in uppercase)
# ----------------------
PI = 3.14159
AWS_REGION = "ap-south-1"

print("Constant PI:", PI)
print("Constant AWS Region:", AWS_REGION)

# ----------------------
# 4. Keywords (cannot be used as identifiers)
# ----------------------
# Example: if, else, for, while, etc.
# Let's use 'if' keyword
if int_literal > 5:
    print("Keyword example: if condition worked!")

# ----------------------
# 5. Identifiers
# ----------------------
# Identifiers = names for variables, functions, etc.
my_variable = "Cloud Learner"
user_name = "Stark"

print("Identifier example (my_variable):", my_variable)
print("Identifier example (user_name):", user_name)

# ----------------------
# 6. Variables
# ----------------------
a = 100
b = 200
sum_ab = a + b
print("Sum of Variables:", sum_ab)


