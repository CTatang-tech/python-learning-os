## Week 1 Day 4 — Functions

### One-Line Definition
A function is a **named block of reusable logic**.

---

### Why This Matters
Functions:
- reduce duplication
- improve readability
- make testing possible

---

### Structure
```python
def add(a, b):
    return a + b
```
### Mental Model

A function is a machine:

input → processing → output

Defining a function does nothing visible

`print()`- Printing inside a function does not produce a usable value

`return` is the only way data leaves a function
Forgetting to call the function

### Common Confusions

- Thinking def runs the function: 
It doesn’t. It only stores instructions.

- Confusing print with return: print shows something to the screen while return sends a value back to the caller

- Using names before Python knows them: Calling a function before it’s defined,

Using variables inside a function that don’t exist at call time

### Core Rules

DEF stores, CALL runs
return sends a value back
print() only displays

### One-Line Mental Model

A function is stored instructions that only run when explicitly called, in a new execution space, using whatever names exist at that moment.


### Additional terms

**docstrings**
- One rule to remember

A docstring is the first string inside a function, and Python keeps it as the function’s description.

- One-line takeaway

Docstrings don’t make code work — they make code understandable.

```python
def add(a, b):
    """Add two numbers and give the answer back."""
    return a + b
```
- What Python does internally

When Python sees a docstring, it:
Stores it in a special place
Attaches it to the function as metadata
Makes it available to tools like help()

The function still runs the same way.

- Why docstrings matter (even for beginners)

They help you:
Remember what your function does
Understand old code later
Read other people’s code
Use built-in help tools

Big programs live on docstrings.