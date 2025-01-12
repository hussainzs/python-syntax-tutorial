## **1. Python Basics**

### **2.1 Syntax and Indentation**

####  Importance of Indentation (Space at beginning of the line)
In Python, indentation is not just for readability—it defines the structure and flow of the program.
- **Significance:** Unlike many other programming languages that use braces `{}` to denote code blocks, Python uses indentation. 

**Example:**
```python
# Correct indentation
if True:
    print("This is indented correctly.")
    print("Still within the if block.")

# Incorrect indentation (will raise an IndentationError)
if True:
print("This will cause an error.")
```

#### Basic Syntax Rules

- **Case Sensitivity:** Python is case-sensitive (`Variable`, `variable`, and `VARIABLE` are different).
- **Comments:** Use `#` for single-line comments and triple quotes `'''` or `"""` for multi-line comments/docstrings.
```python
# This is a single-line comment

""" This is a multi-line 
    comment or docstring to define a function or class.
    # even this is okay here because the # is just part of the string
"""
```

- **[Line Continuation](https://docs.python.org/3.12/reference/lexical_analysis.html#explicit-line-joining):** Two or more physical lines may be joined into logical lines using backslash characters (\)
```python
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1
```
Line Continuation in Python is also possible inside parentheses `()`, brackets `[]`, and braces `{}` without using the backslash character.
```python
my_list = [1, 2, 3, # a comment may appear here no problem
           4, 5, 6]

my_dict = {'key1': 'value1',  # another comment
           'key2': 'value2',
           'key3': 'value3'}  # comment here too if you wish
```

- **[Reserved Keywords](https://docs.python.org/3.12/reference/lexical_analysis.html#identifiers):** Python has reserved words that cannot be used as identifiers.
```python
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

---

### **2.2 Variables and Data Types**

#### **2.2.1 Declaring Variables**
Variables are used to store data. They are created by assigning a value to a name.
- **Naming Rules:**
  - Must start with a letter (a-z, A-Z) or an underscore `_`. NOT by anything else.
  - Can contain letters, digits (0-9), and underscores.
  - Case-sensitive.
  - Should not be a reserved keyword.

**Example:**
```python
# Valid variable names
my_variable = 5 # snake_case
_age1 = 30 # inside a class, _ prefix indicates a private variable or method
firstName = "John" # camelCase

# Invalid variable names (will raise SyntaxError)
2nd_place = "Alice"  # Starts with a digit
$price = 100         # variables cannot start with anything else than a letter or underscore
class = "Math"       # 'class' is a reserved keyword
```

#### **2.2.2 Built-in Data Types**

Python has several built-in data types that are fundamental to writing programs. The primary data types covered here are integers, floats, strings, and booleans.

##### [Numeric Data Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
1. **Integers (`int`):**
   - Whole numbers without a decimal point.
   - Can be positive, negative, or zero.
   - Large numbers are represented in scientific notation (e.g., `1e9` for 1 billion).
   - Immutable, meaning they cannot be changed once created. Pass by value not by reference.
   > **Pass by Value** means that the function is called with a copy of the argument (the value), not the actual argument.

   ```python
   age = 25
   score = -100
   ```

2. **Floats (`float`):**
   - Numbers with a decimal point.
   - Can represent real numbers, including positive, negative, and zero.
   - Large numbers are represented in scientific notation (e.g., `1.0e-3` for 0.001).
   - Immutable, meaning they cannot be changed once created. Pass by value not by reference.

   ```python
   height = 5.9
   temperature = -23.5
   ```
3. **Complex Numbers (`complex`):**
   - Numbers with a real and imaginary part.
   - Written in the form `a + bj`, where `a` and `b` are floats and `j` is the imaginary unit.

   ```python
   z = 3 + 4j
   ```
##### [Text Sequence - str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

4- **Strings (`str`):**
   - Sequences of characters enclosed in single quotes `' '` or double quotes `" "` or triple quotes `''' '''` or `""" """`.
   - Can include letters, numbers, symbols, and whitespace.
   - Immutable, meaning they cannot be changed once created. If you need to modify a string, you create a new one.
```python
name = "Alice"
message = 'Hello, World!'
multiline = '''This is a 
                multi-line string'''
```

4. **Booleans (`bool`):**
   - Represents one of two values: `True` or `False`. Note, they are case-sensitive.
   - Here are most of the built-in objects considered false (example below)
   > constants defined to be false: `None` and `False`. 
   > zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
   > empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`
```python
is_student = True

list = []
print(bool(list))  # Output: False

int = 0
print(bool(int))  # Output: False

dict = None
print(bool(dict))  # Output: False
```

**Additional Data Types (Brief Overview):**
- **[Lists](https://docs.python.org/3/library/stdtypes.html#lists) (`list`):** Ordered, mutable collections.
- **[Tuples](https://docs.python.org/3/library/stdtypes.html#tuples) (`tuple`):** Ordered, immutable collections.
- **[Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) (`dict`):** Unordered, mutable collections of key-value pairs.
- **[Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) (`set`):** Unordered collections of unique elements.

#### **2.2.3 Dynamic Typing in Python**

**Explanation:**
- **Definition:** Python uses dynamic typing, meaning that variable types are determined at runtime and can change as the program executes.
- **Implications:**
  - Flexibility in assigning different data types to the same variable.
  - No need to declare variable types explicitly.
  - Potential for type-related runtime errors if not managed carefully.

**Example:**
```python
# Variable initially assigned an integer
x = 10
print(x)        # Output: 10
print(type(x))  # Output: <class 'int'>

# Reassigning the same variable to a string
x = "Ten"
print(x)        # Output: Ten
print(type(x))  # Output: <class 'str'>

# Reassigning to a float
x = 10.5
print(x)        # Output: 10.5
print(type(x))  # Output: <class 'float'>
```

**Output:**
```
10
<class 'int'>
Ten
<class 'str'>
10.5
<class 'float'>
```

**Considerations:**
- **Type Checking:** Use the `type()` function to check a variable's type.
- **Type Conversion:** Convert between types using functions like `int()`, `float()`, `str()`, etc.

**Example of Type Conversion:**
```python
num_str = "100"
num_int = int(num_str)     # Converts string to integer
num_float = float(num_int) # Converts integer to float

print(num_int)    # Output: 100
print(type(num_int))  # Output: <class 'int'>
print(num_float)  # Output: 100.0
print(type(num_float)) # Output: <class 'float'>
```

**Output:**
```
100
<class 'int'>
100.0
<class 'float'>
```

---

## **Summary**

Understanding Python's syntax and indentation is crucial, as they define the structure and flow of your code. Variables in Python are dynamically typed, allowing flexibility in assigning different data types without explicit declarations. Mastery of these basics lays a strong foundation for advancing to more complex programming concepts.

---

### **Practice Exercises**

1. **Indentation Practice:**
   - Write an `if-else` statement that checks if a number is positive, negative, or zero, and prints an appropriate message. Ensure correct indentation.

2. **Variable Naming:**
   - Declare variables with valid and invalid names. Observe the behavior and understand the naming rules.

3. **Data Types Manipulation:**
   - Assign different data types to a single variable and use the `type()` function to print their types.
   - Convert a string containing a number to an integer and perform an arithmetic operation.

**Example Solution for Exercise 3:**
```python
# Assign different data types to the same variable
var = "Python"
print(var, type(var))  # Output: Python <class 'str'>

var = 3.14
print(var, type(var))  # Output: 3.14 <class 'float'>

var = True
print(var, type(var))  # Output: True <class 'bool'>

# Type conversion and arithmetic operation
num_str = "50"
num_int = int(num_str)
result = num_int + 25
print(result)  # Output: 75
```

**Output:**
```
Python <class 'str'>
3.14 <class 'float'>
True <class 'bool'>
75
```

---

### **Further Reading**

- [Python Official Documentation: Data Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [W3Schools Python Indentation](https://www.w3schools.com/python/python_indentation.asp)

---

This content should provide a solid foundation for your tutorial on Python basics, covering essential aspects of syntax, indentation, variables, data types, and dynamic typing with clear explanations and practical examples.