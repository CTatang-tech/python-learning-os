
**Never start coding on line 1 vscode**

# Rules for VARIABLES
- A variable is a name pointing to a value, not a container holding it.
- Reassigning a variable changes what the name refers to; it does not modify other variables.
- If changing one variable surprises me, I should check whether I’m confusing names with values.

# Notebook rules
- If you didn’t run it in order, you didn’t really test it. (misleading if am careless)

# Core Rule for pyton execution model
Python does NOT look ahead. It only knows what has already executed.

# Rules for data types
-Dynamic Typing: Variables can hold any type, but the operation's success depends on the types at runtime.
- Incompatible Operations: Mixing incompatible types (e.g., numbers and strings) raises TypeError.
- Compatible Operations: Operations work when types are the same or have defined behaviors (e.g., numeric types can mix in some cases).

# Python Operators Examples

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

# Rules for Expression and Statements
- Expressions return values (you can store it, print it, or combine it).
- Statements control behavior (assign, loop, branch, define, import).
- SyntaxError happens before running (Python can’t parse your code)

# Rules for data flow and mini pipelines

- Data must exist BEFORE a step uses it (or NameError happens).
- Expressions produce VALUES; statements perform ACTIONS (assign/print/if/for/def/import).
- Order matters: pipelines are linear; each step depends on the previous step’s output.
- Type matters: wrong types cause TypeError OR silent logic bugs.
- Parentheses change evaluation order and can change results.