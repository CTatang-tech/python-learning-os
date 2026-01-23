
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

# Rules for += operator (compound assignment, e.g x += 1 same as x = x + 1)
- += is a compound assignment that rebinds a name to a new value, after evaluating an expression.
- += is shorthand for “use the old value to compute a new one, then update what the name refers to.
- x += y always depends on the current value of x
- For immutable types, += creates a new value and rebinds
- For mutable types, += may modify the object in place

# Rules for loops (for/while)

**Misunderstanding loop variable “scope” (it still exists after the loop)**
```python 
for k in range (3)
```
Python does this:

First round:
“Here, k, wear the number 0”

Second round:
“Now k, wear the number 1”

Third round:
“Now k, wear the number 2”

Each time, Python reuses the same name tag called k
It just changes the number written on it.

```python
print("k after loop is:", k)
```
Python says:

“Oh! I still know k.
The last number on k’s tag is 2.”

So it prints:

```python
k after loop is: 2
```

# Rules for term `break`
break is a control-flow keyword (a statement)

**What Python does internally when it sees break**

*Inside a loop, Python normally does:*
Get next value
Run loop body
Go back to the top

*When Python executes break, it instead does:*
Stop the loop immediately
Jump to the first line after the loop
Continue normal execution

No more iterations. No questions. No cleanup inside the loop.

**Where `break` is allowed (important rule)**
*break can ONLY appear:*
Inside for loops
Inside while loops
If Python sees break anywhere else → SyntaxError
Because it wouldn’t know what to break out of.

# `break` vs `continue`
- `break` exits the loop.
What Python does :
End the loop immediately and jump outside it.

Nothing else in the loop runs.
No more items are checked.

```python
for n in [2, 4, 6, 7, 8]:
    print("checking", n)
    if n == 7:
        print("found 7 → BREAK")
        break
    print("still inside loop after check")
print("done")
```

- `continue` skips the current iteration.
What Python does: 
Skip the rest of the current loop body and go to the NEXT iteration.

The loop itself does not stop.

```python
for n in range(6):
    if n % 2 == 0:
        print("even → skip body for", n)
        continue
    print("odd → run body for", n)
```

# Rules for `return`
- `return` exits a function

**What return actually does:**
Only works inside functions

Stops the entire function

Sends a value back (or None)

Execution jumps to the caller

# Rules for functions
- **DEF stores, CALL runs.**
- Function body is skipped
- Code inside runs only when called
- `return` sends a value back
- `print()` only displays
- Names must exist **before** they’re used (including function names).
- Function variables live **inside** the function unless returned.
- Errors inside the function usually happen at **call time**, not def time.

# HOW ERRORS ARISE (EXECUTION VIEW)

**SyntaxError**

Python cannot parse the code

Happens before execution

Nothing runs

**NameError**

Python tries to use a name that does not exist yet

Happens at the exact line of use

Common causes:

calling before def

using variable before assignment

👉 Python only knows what has already run.

**TypeError**

Operation attempted on incompatible types

Happens at runtime

Very common inside loops and functions

👉 Python checks types only when the operation happens.

**Logic Errors (Silent Failures)**

Code runs, output is wrong

Causes:

wrong condition order

wrong loop bounds

print instead of return

string vs numeric comparison

👉 No traceback ≠ correct logic.

# HOW TO THINK WHEN CODE FAILS

**Traceback Reading**

Read bottom → up

Last line = where Python failed

Upper lines = how Python got there

# Reorder Before Rewriting

Fix bugs by:

moving def above calls

defining variables earlier

reordering if / elif

moving loop updates inside loops

👉 Same logic, correct execution order.

# Short-circuit Logic rules

- `and / or` may skip checks.

- `and` stops at False

- `or` stops at True

- Some expressions may never be evaluated at all. 

**FINAL NAMEERROR + SHORT-CIRCUIT RULESET**

Memorize this block — it’s production-grade:

`and` hides bugs only while the left side is False

`or` hides bugs only while the left side is True

Short-circuit resets every loop iteration

A NameError can stay hidden for months, then explode when data flips

Always group complex conditions with explicit parentheses

# correct framing (`tuples` vs `list`)

`Tuple` = fixed structure, read-only after creation, immutable

`List` = working container, meant to evolve, mutable

Name rebinding ≠ object mutation

Tuples are for stability, not convenience.