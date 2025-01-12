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

### **2.3 Built-in Datatype Details**


### **2.3.1 Strings: F-Strings (Formatted String Literals)**

**Overview:**
- **Introduced in Python 3.6**, F-strings (`f` or `F`) provide an efficient way to embed expressions directly within string literals.
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
  - Format is defined by width, precision, and type (e.g., `f` is float precision type) i.e. `{value:width.precisiontype}`.
  - **Width:** How many characters the string should be. Padded with spaces if needed.
  - **Precision:** Number of decimal places. rounded to fit.
  > Other useful format specifiers include `:b` for binary, `:e` for scientific notation, and `:%` for percentage.
```python
height = 5.6789
print(f"Height: {height:.1f}") # Output: Height: 5.7
  
num = 19
print(f"{num:b}") # Output: 10011

percent = 65/100
print(f"{percent:%}") # Output: 65.000000%
print(f"{percent:.2%}") # Output: 65.00%

percent = 4531
print(f"{percent:.2e}") # Output: 4.53e+03
```

- **Date Formatting:**
  - Use date format directives to display dates in a specific format:
  - **Directives:** Special codes that start with `%` to represent date components.
  
| Directive | Meaning                            | Example Output       |
|-----------|------------------------------------|----------------------|
| `%A`      | Full weekday name                 | `Friday`            |
| `%B`      | Full month name                   | `January`           |
| `%d`      | Day of the month (zero-padded)    | `27`                |
| `%Y`      | Year with century as decimal      | `2017`              |
| `%H`      | Hour (24-hour clock)              | `15`                |
| `%M`      | Minute                            | `45`                |
| `%S`      | Second                            | `30`                |


```python
from datetime import datetime
today = datetime(2017, 1, 27)

# print without directives
print(f"{today}") # Output: 2017-01-27 00:00:00

print(f"{today:%A, %B %d, %Y}") # Output: Friday, January 27, 2017
```

- **Escaping Braces:**
  - Use double curly braces `{{` and `}}` to include literal braces.
  ```python
  print(f"{{Hello}}")
  # Output: {Hello}
    ```
### **2.3.2 [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not): `and`, `or`, `not`**
 
Boolean operations in Python are used for logical decision-making. They operate on Boolean values (`True`, `False`)

1. **`x or y`**
   - **Result:** Returns True if either `x` or `y` is True, otherwise False. 
   - **Short-Circuit Behavior:** Stops evaluating if `x` is True i.e. If x is True, the result is x, else y (this is often used in web development rendering)

```python
a = 0
b = 10
print(a or b)  # Output: 10 because a is evaluated as False (since its 0) and b is evaluated as True (since non-zero). Thus, the expression is (False OR True) = True
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
   > You can use this short circuit for minor optimizations in your code. Such as if you have two conditions and the first one is more likely to be false, you can put it first or put the condition that's quicker to check first.

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
### **2.3.3 Comparisons**

Python supports eight comparison operations, all of which have the same priority.

#### **Comparison Operators**

| **Operation** | **Meaning**                  |
|---------------|------------------------------|
| `<`           | Strictly less than           |
| `<=`          | Less than or equal           |
| `>`           | Strictly greater than        |
| `>=`          | Greater than or equal        |
| `==`          | Equal                        |
| `!=`          | Not equal                    |
| `is`          | Object identity              |
| `is not`      | Negated object identity      |

**Additional Operators**

| **Operation** | **Meaning**                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `in`          | Checks if an element exists in an iterable (`__contains__` method).         |
| `not in`      | Checks if an element does **not** exist in an iterable (`__contains__`).    |

---

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
- The `in` and `not in` operators are supported by objects implementing the `__contains__` method, such as lists, strings, and dictionaries.

>**Warning:** Avoid using `is` and `is not` to compare values. Use `==` and `!=` for value comparisons. `is` and `is not` are used to compare object identities.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True
print(a is b)  # Output: False since they are different objects in memory with different memory addresses

c = a
print(a is c)  # Output: True since they are the same object in memory which means they both point to the same memory location (same reference)
```
```python
# Wrong use of is
x = 10
y = 10
print(x is y)  # Output: True (unexpected result because of integer caching outside of the scope of this tutorial)
```