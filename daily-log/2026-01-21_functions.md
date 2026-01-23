
# Daily Learning Log — Date:2026-01-21

## FUNCTIONS

## Session Goals for Today
Big idea:
Python does two different things with functions:

It defines them (stores instructions)

It runs them only when called

Python still executes the file top → bottom, but function bodies are skipped until invoked.

**Focus topics:**
- Function definition vs execution
- How Python stores a function in memory
- What happens when a function is called
- Order of execution: define first, call later
- Common function-related execution errors

**What I plan to do:**

1️⃣ Read Concept Note — Python Functions (Execution View)

Focus on:

What Python does at def time

What Python does at call time

Why defining a function does not run its body

2️⃣ Write Execution Predictions (Before Running)

Before running any cell, I will predict:

Which lines execute immediately

Which lines are stored but skipped

When the function body will actually run

What values exist before and after a function call

👉 Key question:

“Has this function been called yet, or only defined?”

3️⃣ Trigger Common Function Errors (On Purpose)

I will intentionally cause:

NameError by calling a function before it is defined

NameError by using a variable inside a function that doesn’t exist

Confusion between defining a function and executing it

Then I will:

Predict the error

Run the code

Compare prediction vs reality

4️⃣ Reorder Code to Make It Work

I will:

Move function definitions above function calls

Separate:

Setup phase (definitions)

Execution phase (calls)

Observe how reordering lines fixes errors without changing logic

👉 Key realization:
Python does not “look ahead.”
It only knows what has already been executed.

5️⃣ Explain Each Outcome in Plain English

For every result or error, I will explain:

What Python knew at that line

What Python did not know yet

Why the function body ran (or didn’t)

Why the error happened at that exact line

No jargon.
If I can’t explain it simply → I don’t understand it yet.

---

**Planned Experiments**

Below is a **ready-to-run experiment pack** (cells + prompts) you can paste directly into `sandbox.ipynb`.

**Rule:** For each cell → **PREDICT first** (in a markdown line), then run.

---

# 🧪 FUNCTIONS — Execution-First Experiment Pack (Notebook Ready)

## ✅ Cell 0 — Session Header (Markdown)

**Copy into a Markdown cell:**

* **Today’s concept:** FUNCTIONS
* **Key rule:** **`DEF` stores, CALL runs**
* **Prediction habit:** “Has it been **called** yet, or only **defined**?”

---

## Experiment 1 — DEF time vs CALL time

### ✅ Cell 1 — “DEF stores, CALL runs”

```python
print("Top of cell: start")

def greet():
    print("Inside greet(): running the body")

print("After def: greet is now a name in memory")

greet()

print("Bottom of cell: end")
```

**Predict:**

1. Which lines run immediately?
2. Which line is **stored but skipped**?
3. Exact print order?

---

### ✅ Cell 2 — Prove the body is skipped until called

```python
def loud():
    print("LOUD BODY RUNNING!")

print("About to NOT call loud()")
print("Done")
```

**Predict:** Will `"LOUD BODY RUNNING!"` appear? Why?

---

## Experiment 2 — NameError traps (calling too early / missing names)

### ✅ Cell 3 — Call before def (NameError)

```python
say_hi()  # calling before definition

def say_hi():
    print("hi")
```

**Predict:**

* Error type?
* Exact failing line?
* What did Python “not know yet”?

---

### ✅ Cell 4 — Using a name inside a function that doesn’t exist (NameError at CALL time)

```python
def report():
    print("report() started")
    print(score)  # score does not exist yet

print("Defined report()")

report()
```

**Predict:**

* Does the error happen at **def time** or **call time**?
* Why?

---

### ✅ Cell 5 — Fix by defining the name before the call

```python
def report():
    print("report() started")
    print("score =", score)

score = 99
report()
```

**Predict:** What prints now?

---

## Experiment 3 — Reordering fixes errors without changing logic

### ✅ Cell 6 — Broken order

```python
total = add(2, 3)
print("total =", total)

def add(a, b):
    return a + b
```

**Predict:** What error and why?

---

### ✅ Cell 7 — Working order (same logic, correct order)

```python
def add(a, b):
    return a + b

total = add(2, 3)
print("total =", total)
```

**Predict:** Output?

---

## Experiment 4 — Return vs Print (VALUE vs ACTION)

### ✅ Cell 8 — print() returns None (classic confusion)

```python
def f():
    print("I print, but I return nothing")

result = f()
print("result is:", result)
```

**Predict:**

* What prints from inside `f()`?
* What is `result`?

---

### ✅ Cell 9 — return gives a value you can use

```python
def g():
    return "HELLO"

x = g()
print("x =", x)
print("x.lower() =", x.lower())
```

**Predict:** What prints?

---

## Experiment 5 — Local scope vs global (NameError + “function has its own room”)

### ✅ Cell 10 — Local variable does not exist outside (NameError)

```python
def make_number():
    n = 7
    print("inside:", n)

make_number()
print("outside:", n)
```

**Predict:**

* What prints?
* What error happens and why?

---

### ✅ Cell 11 — Fix: return the value

```python
def make_number():
    n = 7
    return n

outside_n = make_number()
print("outside_n:", outside_n)
```

**Predict:** Output?

---

## Experiment 6 — “Names are resolved at CALL time” (a sneaky mental model)

### ✅ Cell 12 — Define first, create variable later, then call (works)

```python
def show():
    print("value =", value)

value = 123
show()
```

**Predict:** Does it work? Why?

---

### ✅ Cell 13 — Call before variable exists (fails)

```python
def show():
    print("value =", value)

show()
value = 123
```

**Predict:** Error type? Why *here*?

---

## Experiment 7 — Default arguments are “captured” at DEF time (important rule)

### ✅ Cell 14 — Default argument trap

```python
x = 10

def use_default(n=x):
    print("n =", n)

x = 99
use_default()
use_default(x)
```

**Predict:**

* What does `use_default()` print?
* Why is it not using the new `x`?

---

## Experiment 8 — Short traceback reading drill (practice your narration)

### ✅ Cell 15 — One bug, one fix

```python
def half(n):
    return n / 2

print(half("8"))
```

**Predict:**

* Error type?
* What operation caused it?
* Fix idea (in plain English)?

Then fix it in a new cell:

```python
def half(n):
    return n / 2

print(half(int("8")))
```

---

# 🔥 Rules to Record Today (copy into `rules_i_learned.md`)

1. **DEF stores, CALL runs.**
2. Python executes **top → bottom**; it doesn’t “look ahead.”
3. Names must exist **before** they’re used (including function names).
4. Function variables live **inside** the function unless returned.
5. Errors inside the function usually happen at **call time**, not def time.

---

**Succes criteria:**
✅ I can explain why defining a function does not run it
✅ I can predict when a function body will execute
✅ I can explain why calling a function before its definition fails
✅ I can explain function execution using a top-to-bottom mental model
✅ I recorded at least one reusable execution rule about functions

--- 

