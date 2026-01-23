
---

# 📘  Loops (`for` & `while`)

```md
## Week 1 Day 3 — Loops

### One-Line Definition
Loops allow Python to **repeat actions** without rewriting code.

---

### Why This Matters
Loops are essential for:
- processing data
- automation
- scaling logic

---

### Loop Types
- `for` → iterate over a collection
- `while` → repeat while a condition is true

---

### Mental Model
A loop is a **factory machine**:
- same action
- applied repeatedly
- controlled entry/exit

**Loops — Python’s Repetition Engine**

*What happens internally:*

Python enters a loop
Assigns a value to the loop variable
Runs the body top-to-bottom
Decides whether to repeat or exit

*Important mental shift:*

A loop variable is one reusable name, not a new variable each time.

That’s why the loop variable still exists after the loop, holding the last assigned value.

---

**`+=` Recompute, Then Rebind (or Mutate)**
*What Python does internally*

Look up the current object bound to the name
Evaluate the right-hand expression
Decide:
    Immutable object → create a new object, rebind the name

    Mutable object → modify the same object in place

So `+=` is not “add something”
It is:

“Use the old value to compute a new state, then update the name’s reference.”

---

**Mutability — The Hidden Decider**

*Mutability answers one critical question:*

`Does Python update the object, or replace it?`

**Immutable** (int, str, tuple): object cannot change → rebinding happens

**Mutable** (list, dict, set): object can change → same object, new contents

This explains:

Why lists “change everywhere”

Why integers never do

Why += behaves differently depending on the type

---

**break vs continue vs return**
What Python does when it sees them

`break`
Immediately exits the nearest loop
Jumps to the first line after the loop

`continue`
Skips the rest of the current iteration
Goes straight to the next loop check

`return`
Stops the entire function
Sends a value back to the caller
No further lines in the function run

These are execution jump commands, not logic checks.

---

### Common Loop Bugs
- Infinite loops
- Off-by-one errors
- Modifying data while looping
- Thinking loop variables disappear: They don’t — Python just stops reassigning them.
- Assuming += always creates a new value
It depends on mutability, not the operator.
- Using break or continue outside a loop
Python raises SyntaxError because there’s nothing to jump out of.

---

### Core Rules
- `for` loops iterate over sequences
- `while` loops need exit conditions
- Every loop must eventually stop

### Rules 
Mutability decides: update (mutable-object changes internally) vs replace (immutable-object can not change internally)

Control-flow keywords don’t compute — they redirect execution

### One-Line Mental Model

Python executes line-by-line, reusing names, updating or replacing objects based on mutability, and jumping only when explicitly told to.