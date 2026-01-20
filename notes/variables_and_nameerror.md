## Day 2 — Variables & NameError

### One-Line Definition
A variable is a **name bound to a value** in memory.

---

### Why This Matters
Without variables:
- You can’t store results
- You can’t reuse data
- Programs become impossible to scale

---

### Mental Model
A variable is a **label stuck on a box**.
The label must exist before you can use it.

---

### NameError Explained
`NameError` happens when Python sees a name that:
- has never been defined
- or was defined later (hasn’t executed yet)

---

### Example

```python

print(x)   # ❌ NameError
x = 10

```
---

### Core Rules
Variables must be defined before use
Python does not guess missing values