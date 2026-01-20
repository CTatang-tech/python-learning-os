
# 📘 Day 3 Concept — Types & TypeError

## Day 3 — Types & TypeError

### One-Line Definition
A type describes **what kind of value** something is.

---

### Why This Matters
Types determine:
- What operations are allowed
- What errors you get
- How data behaves

---

### Core Types
- `int` → whole numbers
- `float` → decimals
- `str` → text
- `bool` → True / False

---

### Mental Model
- Variables in Python are dynamically typed—x can hold any type, and type() reveals the current type. The "same value" (5) is represented differently across types

---
### TypeError Explained
`TypeError` occurs when you:
- combine incompatible types
- use an operation on the wrong type

---

### Beginner Mistakes
Here are 3 common beginner mistakes that lead to TypeErrors, along with explanations:

**Adding a string and an integer**  
```python
"10" + 5  # ❌ TypeError: can only concatenate str (not "int") to str
```  
**Why it fails:** Python doesn't automatically convert types. The `+` operator for strings means concatenation, but you can't concatenate a string with an integer. You need to convert one to match the other, like `int("10") + 5` or `"10" + str(5)`.

**Multiplying a string by a float**  
```python
"hello" * 2.5  # ❌ TypeError: can't multiply sequence by non-int of type 'float'
```  
**Why it fails:** The `*` operator for strings repeats the string, but it requires an integer count. Floats aren't allowed because repetition must be a whole number. Convert to int first: `"hello" * int(2.5)`.

**Using len() on an integer**  
```python
len(123)  # ❌ TypeError: object of type 'int' has no len()
```  
**Why it fails:** `len()` works on sequences like strings, lists, or tuples, not on numbers. Integers don't have a length. If you meant to count digits, convert to string: `len(str(123))`.

### Casting 
You must explicitly convert types:
```python
int("10") + 5
```
- int(value): Converts to integer (e.g., from str or float).
- float(value): Converts to float (e.g., from int or str).
- str(value): Converts to string (e.g., from int, float, or bool).
- bool(value): Converts to boolean (e.g., from int, str, or list; 0, empty strings/lists are - False).
- list(value): Converts to list (e.g., from str, tuple, or set).

**Boolean Casting:**
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("hi"))   # True

----

### Python Operators Examples

**Arithmetic Operators**
5 + 3    # Addition: 8
10 - 4   # Subtraction: 6
6 * 7    # Multiplication: 42
20 / 4   # Division: 5.0
15 // 4  # Floor Division: 3
15 % 4   # Modulus: 3
2 ** 3   # Exponentiation: 8

**Comparison Operators**
5 == 5   # Equal: True
5 != 3   # Not Equal: True
5 > 3    # Greater Than: True
5 < 3    # Less Than: False
5 >= 5   # Greater or Equal: True
5 <= 3   # Less or Equal: False

**Logical Operators**
True and False  # False
True or False   # True
not True        # False

**Assignment Operators**
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x /= 4   # x = 6.0

---

## Core Rules
- Python is strongly typed
- Conversions are explicit, not automatic
- Dynamic Typing: Variables can hold any type, but the operation's success depends on the types at runtime.
- Incompatible Operations: Mixing incompatible types (e.g., numbers and strings) raises TypeError.
- Compatible Operations: Operations work when types are the same or have defined behaviors (e.g., numeric types can mix in some cases).


---
