Most sections are linked to the relevant official Python documentation for further reading.

- Beginner Friendly Python Tutorial by official Python documentation: https://docs.python.org/3.13/tutorial/index.html#tutorial-index
- Python Standard Library reference: https://docs.python.org/3.13/library/index.html#library-index

## **1. [Python Language Reference](https://docs.python.org/3.13/reference/index.html)**

### **2.1 Basic Syntax and Indentation**

#### Importance of Indentation (Space at beginning of the line)

In Python, indentation is not just for readability—it defines the structure and flow of the program.

- **Significance:** Unlike many other programming languages that use braces `{}` to denote code blocks, Python uses
  indentation.

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

- **[Line Continuation](https://docs.python.org/3.12/reference/lexical_analysis.html#explicit-line-joining):** Two or
  more physical lines may be joined into logical lines using backslash characters (\\)

```python
if 1900 < year < 2100 and 1 <= month <= 12
        and 1 <= day <= 31 and 0 <= hour < 24
        and 0 <= minute < 60 and 0 <= second < 60:  # Looks like a valid date
    return 1
```

Line Continuation in Python is also possible inside parentheses `()`, brackets `[]`, and braces `{}` without using the
backslash character.

```python
my_list = [1, 2, 3,  # a comment may appear here no problem
           4, 5, 6]

my_dict = {'key1': 'value1',  # another comment
           'key2': 'value2',
           'key3': 'value3'}  # comment here too if you wish
```

- **[Reserved Keywords](https://docs.python.org/3.12/reference/lexical_analysis.html#identifiers):** Python has reserved
  words that cannot be used as identifiers.

```python
False
await else import

pass
None
break      except in raise
True


class finally    is return

and continue
for lambda try
           as def from nonlocal while
           assert del global not with
           async elif if or yield
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
my_variable = 5  # snake_case
_age1 = 30  # inside a class, _ prefix indicates a private variable or method
firstName = "John"  # camelCase

# Invalid variable names (will raise SyntaxError)
2
nd_place = "Alice"  # Starts with a digit
$price = 100  # variables cannot start with anything else than a letter or underscore


class = "Math"  # 'class' is a reserved keyword
```

#### **2.2.2 Built-in Data Types**

Python has several built-in data types that are fundamental to writing programs. The primary data types covered here are
integers, floats, strings, and booleans.

##### [Numeric Data Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

1. **Integers (`int`):**
    - Whole numbers without a decimal point.
    - Can be positive, negative, or zero.
    - Large numbers are represented in scientific notation (e.g., `1e9` for 1 billion).
    - Immutable, meaning they cannot be changed once created. Pass by value not by reference.
   > **Pass by Value** means that the function is called with a copy of the argument (the value), not the actual
   argument.

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

4- **[Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)) (`str`):**

- Sequences of characters enclosed in single quotes `' '` or double quotes `" "` or triple quotes `''' '''`
  or `""" """`.
- Can include letters, numbers, symbols, and whitespace.
- Immutable, meaning they cannot be changed once created. If you need to modify a string, you create a new one.

```python
name = "Alice"
message = 'Hello 2 World!'
multiline = '''This is a #42^5$
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

**Additional Data Types (Brief definitions for now):**

- **[Lists](https://docs.python.org/3/library/stdtypes.html#lists) (`list`):** Ordered, mutable collections.
- **[Tuples](https://docs.python.org/3/library/stdtypes.html#tuples) (`tuple`):** Ordered, immutable collections.
- **[Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) (`dict`):** Unordered, mutable
  collections of key-value pairs.
- **[Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) (`set`):** Unordered collections of
  unique elements.

#### **2.2.3 Dynamic Typing in Python**

- Python uses dynamic typing, meaning that variable types are determined at runtime and can change as
  the program executes.
- Type Annotations are strongly recommended for better code readability and maintainability. 
> However, a common misconception is that type annotations make code faster or enforce type checking. They do not. They simply provide hints to developers and tools.

> Read the Best Practices here: https://typing.readthedocs.io/en/latest/reference/best_practices.html

> For a list of built-in types, examples on type hinting for functions and classes, check out this: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

```python

**Example:**

```python
# Variable initially assigned an integer
x = 10
print(x)  # Output: 10
print(type(x))  # Output: <class 'int'>

# Reassigning the same variable to a string
x = "Ten"
print(x)  # Output: Ten
print(type(x))  # Output: <class 'str'>

# Reassigning to a float
x = 10.5
print(x)  # Output: 10.5
print(type(x))  # Output: <class 'float'>
```

## **3. Built-in Datatype Details**

### **3.1 Strings: [F-Strings](https://docs.python.org/3.13/reference/lexical_analysis.html#formatted-string-literals) (Formatted String Literals)**

**Overview:**

- **Introduced in Python 3.6**: F-strings (`f` or `F`) provide an efficient way to embed expressions directly within
  string literals.
- **Syntax:** Place expressions inside curly braces `{}`. Text outside braces is treated as literal.

- **Basic String Interpolation:**
    - Embed variables directly into strings.
  ```python
  name = "Alice"
  age = 30
  print(f"Name: {name}, Age: {age}")
  # Output: Name: Alice, Age: 30
  ```

- **Debugging with `=`:**
    - Show both the expression and its evaluated value.
  ```python
  print(f"Debug: {age=}")
  # Output: Debug: age=30
  ```

- **Expressions Inside F-Strings:**
    - Use inline expressions like method calls or calculations.
  ```python
  name = "Alice"
  print(f"Uppercase: {name.upper()}")
  # Output: Uppercase: ALICE
  ```

- **Formatting Numbers:**
    - Use format specifiers to control the display of numbers appended by colon :
    - For example, `:.2f` formats a float to two decimal places.
    - Format is defined by width, precision, and type (e.g., `f` is float precision type)
      i.e. `{value:width.precisiontype}`.
    - **Width:** How many characters the string should be. Padded with spaces if needed.
    - **Precision:** Number of decimal places. rounded to fit.
  > Other useful format specifiers include `:b` for binary, `:e` for scientific notation, and `:%` for percentage.

```python
height = 5.6789
print(f"Height: {height:.1f}")  # Output: Height: 5.7

num = 19
print(f"{num:b}")  # Output: 10011

percent = 65 / 100
print(f"{percent:%}")  # Output: 65.000000%
print(f"{percent:.2%}")  # Output: 65.00%

percent = 4531
print(f"{percent:.2e}")  # Output: 4.53e+03
```

- **Date Formatting:**
    - Use date format directives to display dates in a specific format:
    - **Directives:** Special codes that start with `%` to represent date components.

| Directive | Meaning                        | Example Output |
|-----------|--------------------------------|----------------|
| `%A`      | Full weekday name              | `Friday`       |
| `%B`      | Full month name                | `January`      |
| `%d`      | Day of the month (zero-padded) | `27`           |
| `%Y`      | Year with century as decimal   | `2017`         |
| `%H`      | Hour (24-hour clock)           | `15`           |
| `%M`      | Minute                         | `45`           |
| `%S`      | Second                         | `30`           |

```python
from datetime import datetime

today = datetime(2017, 1, 27)

# print without directives
print(f"{today}")  # Output: 2017-01-27 00:00:00

print(f"{today:%A, %B %d, %Y}")  # Output: Friday, January 27, 2017
```

- **Escaping Braces:**
    - Use double curly braces `{{` and `}}` to include literal braces.
  ```python
  print(f"{{Hello}}")
  # Output: {Hello}
    ```

### 3.2 [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not): `and`, `or`, `not`


Boolean operations in Python are used for logical decision-making. They operate on Boolean values (`True`, `False`)

1. **`x or y`**
    - **Result:** Returns True if either `x` or `y` is True, otherwise False.
    - **Short-Circuit Behavior:** Stops evaluating if `x` is True i.e. If x is True, the result is x, else y (this is
      often used in web development rendering)

```python
a = 0
b = 10
print(
    a or b)  # Output: 10 because a is evaluated as False (since its 0) and b is evaluated as True (since non-zero). Thus, the expression is (False OR True) = True
print(False or False)  # Output: False
```

**Use Case:**

   ```python
   username = input("Enter username: ") or "Guest"
print(f"Welcome, {username}!")  # Default to "Guest" if input() outputs empty string which is falsy.
   ```

2. **`x and y`**
    - **Result:** Returns True if both `x` and `y` are True, otherwise False.
    - **Short-Circuit Behavior:** Stops evaluating if `x` is falsy. i.e. If x is False, the result is x, else y.
   > You can use this short circuit for minor optimizations in your code. Such as if you have two conditions and the
   first one is more likely to be false, you can put it first or put the condition that's quicker to check first.

   ```python
   a = 0
   b = 10
   print(a and b)  # Output: 0
   print(b and a)  # Output: 0
   ```

   **Use Case:**
   ```python
   threshold = 50
   score = 75
   print("Pass" if score >= threshold and score <= 100 else "Invalid score")
   ```

3. **`not x`**
    - **Result:** Negates the value of `x`. If `x` is True, returns False. If `x` is False, returns True.
    - **Lower Priority:** `not` has lower precedence than comparison operators like `<`, `>`, `==`, etc.

   ```python
   a = 0
   b = 10
   print(not a)  # Output: True
   print(not b)  # Output: False
   # Lower priority: "not a == b" will be evaluated as "not (a == b)"
   ```

   **Use Case:**
   ```python
   is_logged_in = False
   if not is_logged_in:
       print("Please log in to continue.")
   ```

### **3.3 [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)**

Python supports eight comparison operations, all of which have the same priority.

#### **Comparison Operators**

| **Operation** | **Meaning**             |
|---------------|-------------------------|
| `<`           | Strictly less than      |
| `<=`          | Less than or equal      |
| `>`           | Strictly greater than   |
| `>=`          | Greater than or equal   |
| `==`          | Equal                   |
| `!=`          | Not equal               |
| `is`          | Object identity         |
| `is not`      | Negated object identity |

**Additional Operators**

| **Operation** | **Meaning**                                                              |
|---------------|--------------------------------------------------------------------------|
| `in`          | Checks if an element exists in an iterable (`__contains__` method).      |
| `not in`      | Checks if an element does **not** exist in an iterable (`__contains__`). |

#### **Examples**

- **Basic Comparisons:**
  ```python
  x = 5
  y = 10
  print(x < y)       # Output: True
  print(x >= y)      # Output: False
  ```

- **Equality and Identity:**
  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  c = a
  print(a == b)      # Output: True (same content)
  print(a is b)      # Output: False (different objects)
  print(a is c)      # Output: True (same object)
  ```

- **Chained Comparisons:**
  ```python
  x, y, z = 5, 10, 15
  print(x < y <= z)  # Output: True
  ```

- **Membership Testing:**
  ```python
  nums = [1, 2, 3]
  print(2 in nums)   # Output: True
  print(4 not in nums)  # Output: True
  ```

#### **Notes**

- You may also say, `x < y <= z` which is equivalent to `x < y and y <= z`.
- The `in` and `not in` operators are supported by objects implementing the `__contains__` method, such as lists,
  strings, and dictionaries.

> **Warning:** Avoid using `is` and `is not` to compare values. Use `==` and `!=` for value comparisons. `is`
> and `is not` are used to compare object identities.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True
print(a is b)  # Output: False since they are different objects in memory with different memory addresses

c = a
print(
    a is c)  # Output: True since they are the same object in memory which means they both point to the same memory location (same reference)
```

```python
# Wrong use of is
x = 10
y = 10
print(x is y)  # Output: True (unexpected result because of integer caching outside of the scope of this tutorial)
```

### 3.4[ Operators on Numerical Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex): `int` and `float`

Python provides a variety of operations for working with numerical types such as `int` and `float`. Below is a breakdown
of these operations:

#### **Basic Arithmetic Operations**

- **Addition (`x + y`)**: Adds two numbers.

  ```python
  x = 10
  y = 5
  result = x + y
  print("Sum:", result)  # Output: Sum: 15
  ```

- **Subtraction (`x - y`)**: Subtracts the second number from the first.

  ```python
  x = 10
  y = 5
  result = x - y
  print("Difference:", result)  # Output: Difference: 5
  ```

- **Multiplication (`x * y`)**: Multiplies two numbers.

  ```python
  x = 10
  y = 5
  result = x * y
  print("Product:", result)  # Output: Product: 50
  ```

- **Division (`x / y`)**: Divides the first number by the second and returns a floating-point result.

  ```python
  x = 10
  y = 4
  result = x / y
  print("Quotient:", result)  # Output: Quotient: 2.5
  print(type(result)) # Output: <class 'float'>
  ```

#### **Integer Division and Modulus**

- **Floored Division (`x // y`)**: Returns the quotient of the division, rounded DOWN to the nearest integer.

```python
left = 3
right = 4
mid = (left + right) // 2  # this is how mid is calculated in binary search
print(
    f"Simple Integer Division: {(left + right) / 2}")  # Output: 3.5 (in binary search we need an integer index not float like 3.5)
print("Floored Quotient:", mid)  # Output: 3
```

- **Modulus (`x % y`)**: Returns the remainder of the division.

```python
x = 10
y = 3
print("Remainder:", x % y)  # Output: Remainder: 1
print("Remainder:", y % x)  # Output: Remainder: 3 (for any x % y, if x < y, the result is x)
```

```python
# Example: Check if a number is even or odd
num = 10
print("Even") if num % 2 == 0 else print("Odd")
```

#### **Absolute Value**

- **Absolute (`abs(x)`)**: Returns the absolute value of `x`.

  ```python
  x = -10
  print("Absolute Value:", abs(x))  # Output: Absolute Value: 10
  ```

#### **Type Conversion**

- **Convert to Integer (`int(x)`)**: Converts a float or string to an integer (truncating the fractional part for
  floats).

```python
x = 3.7
print("Integer:", int(x))  # Output: Integer: 3

someString = "182"
print(int(someString))  # Output: 182

someString = "  182  "  # spaces are ignored
print(int(someString))  # Output: 182

someString = "182.5"  # decimal point is not allowed for int() conversion from string
print(int(someString))  # Output: ValueError: invalid literal for int() with base 10: '  182.5  '

someString = "a2b2"  # alphabets are not allowed
print(int(someString))  # Output: ValueError: invalid literal for int() with base 10: 'a2b2'
```

- **Convert to Float (`float(x)`)**: Converts an integer or string to a floating-point number.

  ```python
  x = 3
  print("Float:", float(x))  # Output: Float: 3.0
  ```

#### **Exponents and Power**

- **Power (`pow(x, y)` or `x ** y`)**: Raises `x` to the power of `y`.

  ```python
  x = 2
  y = 3
  print("Power (pow):", pow(x, y))  # Output: Power (pow): 8
  print("Power (**):", x ** y)  # Output: Power (**): 8
  print(pow(0,0)) # Output: 1 (0^0 = 1) a common mathematical convention 
  ```

- **Divmod (`divmod(x, y)`)**: divmod(x,y) = (x // y, x % y). Returns a tuple containing the floored quotient and
  remainder of the division.

  ```python
  x = 10
  y = 3
  print("Divmod:", divmod(x, y))  # Output: Divmod: (3, 1)
  print("Divmod:", divmod(y, x))  # Output: Divmod: (0, 3)
  ```

#### **Notes**

1. The modulus operator (`%`) and floored division work consistently with negative numbers.
2. Conversion from `float` to `int` truncates the decimal part.
3. `float()` accepts strings like "+inf" or "-nan" to represent infinity or NaN.

### 3.5 [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

Python provides many built-in methods to work with strings. Below are some of them but checkout the documentation for a
complete list.

- **`str.upper()`**: Converts all characters in the string to uppercase.

  ```python
  text = "hello world"
  print(text.upper())  # Output: HELLO WORLD
  ```

- **`str.lower()`**: Converts all characters in the string to lowercase.

  ```python
  text = "HELLO WORLD"
  print(text.lower())  # Output: hello world
  ```

- **`str.capitalize()`**: Capitalizes the first character of the string.

  ```python
  text = "hello world"
  print(text.capitalize())  # Output: Hello world
  ```

- **`str.title()`**: Capitalizes the first character of each word.

  ```python
  text = "hello world"
  print(text.title())  # Output: Hello World
  ```

#### **2. String Search and Replace**

- **`str.find(substring)`**: Returns the index of the first occurrence of `substring` in the string, or `-1` if not
  found.

  ```python
  text = "hello world"
  print(text.find("world"))  # Output: 6
  ```

- **`str.replace(old, new, count=-1)`**: Replaces all occurrences of `old` with `new`.

> Python 3.13+ allows you to use `count` parameter to specify the number of occurrences to replace.
> If count is given, only the first count occurrences are replaced. If count is not specified or -1, then all occurrences
> are replaced.

```python
text = "X is crazy, X is a genius, X is a fool, X is a hero"
print(text.replace("X", "Z", count=2))  # Output: Z is crazy, Z is a genius, X is a fool, X is a hero
text = "X is crazy, X is a genius, X is a fool, X is a hero"
print(text.replace("X", "Z"))  # Output: Z is crazy, Z is a genius, Z is a fool, Z is a hero
```

#### **3. String Splitting and Joining**

- **`str.split(delimiter)`**: Splits the string into a list of substrings based on the specified `delimiter`.

```python
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

# fun fact with list
print(list("apple"))  # Output: ['a', 'p', 'p', 'l', 'e']
```

- **`delimiter.join(iterable)`**: Joins elements of an iterable (e.g., list) into a single string using the `delimiter`.

  ```python
  fruits = ["apple", "banana", "cherry"]
  print(",".join(fruits))  # Output: apple,banana,cherry
  ```

#### **4. String Trimming**

- **`str.strip()`**: Removes leading and trailing whitespace.

  ```python
  text = "   hello world   "
  print(text.strip())  # Output: hello world
  ```

- **`str.lstrip()`**: Removes leading whitespace.

  ```python
  text = "   hello world"
  print(text.lstrip())  # Output: hello world
  ```

- **`str.rstrip()`**: Removes trailing whitespace.

  ```python
  text = "hello world   "
  print(text.rstrip())  # Output: hello world
  ```

#### **5. String Validation**

- **`str.isdigit()`**: Returns `True` if all characters in the string are digits.

  ```python
  text = "12345"
  print(text.isdigit())  # Output: True
  ```

- **`str.isalpha()`**: Returns `True` if all characters in the string are alphabetic.

  ```python
  text = "hello"
  print(text.isalpha())  # Output: True
  ```

- **`str.isalnum()`**: Returns `True` if all characters in the string are alphanumeric.

  ```python
  text = "hello123"
  print(text.isalnum())  # Output: True
  ```

## Brief Review of [Objects](https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types)
### 10 Crucial Points to Understand Objects in Python (For Beginners)

1. **Everything is an Object**  
   All data in Python (e.g., integers, strings, lists, functions) is represented as objects. This abstraction allows uniformity in how data and operations are managed.

   ```python
   x = 10  # x is an Object of type int
   print(type(x))  # Output: <class 'int'>
   ```

2. **Identity, Type, and Value**  
   Each object in Python has:
   - **Identity**: A unique identifier, equivalent to the object's memory address.
   - **Type**: Defines the operations an object supports.
   - **Value**: The data the object represents.

   ```python
   x = 10
   print(id(x))  # Unique identity
   print(type(x))  # Object type
   print(x)  # Object value
   ```

3. **Immutability vs Mutability**  
   - **Immutable objects**: Their value cannot change (e.g., `int`, `float`, `str`, `tuple`).
   - **Mutable objects**: Their value can change (e.g., `list`, `dict`).

```python
# Immutable example
x = 10
print(id(x)) # example output: 171357067490663 (varies for each run)
x = x + 1  # New object created with new id
print(id(x)) # example output: 171357067490695 (varies for each run)

# Mutable example
lst = [1, 2, 3]
print(id(lst)) # example output: 928137487123 (varies for each run)
lst.append(4)  # Modified in place
print(id(lst)) # example output: 928137487123 (same as above)
```

4. **The `is` Operator and `id()` Function**  
   - `is`: Checks if two variables point to the same object.
   - `id()`: Returns the identity of an object.

   ```python
   a = 10
   b = 10
   print(a is b)  # Output: True (same object)
   print(id(a), id(b))  # Same ID
   ```

5. **Garbage Collection**  
   Objects are automatically managed by Python's garbage collector. When no references to an object exist, it becomes eligible for cleanup.


6. **Containers and References**  
   - Containers (e.g., `list`, `dict`) hold references to other objects.
   - The container's value reflects the references, not the actual data.

```python
# Create a mutable object (list) and a container (list of lists)
inner_list = [1, 2, 3]
outer_list = [inner_list]  # outer_list holds a reference to inner_list

# Modify the referenced object
inner_list.append(4)

# Both inner_list and outer_list reflect the change
print(inner_list)  # Output: [1, 2, 3, 4]
print(outer_list)  # Output: [[1, 2, 3, 4]]
```

7. **Mutable Objects in Immutable Containers**  
   Immutable containers (e.g., `tuple`) can reference mutable objects, and those referenced objects can change.

```python
twice = ([], "abc")
twice[0].append(5)
print(twice)

# However, if you try to reassign the tuple, it will raise an error
twice[0] = [1,2,3] # output: TypeError: 'tuple' object does not support item assignment
twice[1] = "def" # output: TypeError: 'tuple' object does not support item assignment
```

8. **Shared References**  
   For mutable objects, multiple variables can reference the same object, leading to shared state.

   ```python
   a = [1, 2, 3]
   b = a  # Both reference the same list
   b.append(4)
   print(a)  # Output: [1, 2, 3, 4]
   ```

9. **Object Finalization**  
   Objects managing external resources (e.g., files) should explicitly release them using methods like `close()`. The `with` statement ensures proper cleanup.

   ```python
   with open('file.txt', 'w') as file:
       file.write('Hello, world!')  # File automatically closed
   ```

10. **Optimization for Immutable Objects**  
    Python MAY reuse objects for immutable types with the same value to save memory (Integer Caching)
> Never rely on this behavior for mutable objects 

```python
    a = 256
    b = 256
    print(a is b)  # True (same memory address for small integers: Integer Caching)

    x = 257
    y = 257
    print(x is y)  # False (different memory address for larger integers)
```
> If you are more interested here is some information:

Python implements integer caching with the following rules:
- By default, Python caches integers between -5 and 256 (inclusive)
- When using integers within this range, variables pointing to the same value will reference the same object in memory
- The caching is done at interpreter startup for performance optimization, since these numbers are frequently used

- The REPL (interactive interpreter) strictly follows the -5 to 256 range
- The compiler may optimize and cache additional numbers outside this range in certain situations
- This caching behavior applies to integers only, though some implementations may also cache certain float values
