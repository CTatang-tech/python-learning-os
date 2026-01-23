

# Daily Learning Log — Date:2026-01-21

## CONDITIONAL LOGIC (if / elif / else)

## Session Goals for Today
Understand how Python makes decisions, and how it chooses exactly ONE path in an if / elif / else block while still executing code top-to-bottom.

Big idea: Python reads conditions in order, stops at the first True, and skips the rest.

**Focus topics:**
- Conditional evaluation order
- Boolean expressions (==, >, <, and, or)
- if vs elif vs else
- Short-circuit behavior
- Why indentation is execution control

**What I plan to do:**

1️⃣ Read Concept Note

📄 Concept: Conditional Logic
Focus on:

How Python evaluates conditions line-by-line

Why only one branch runs

Why order matters more than correctness

2️⃣ Write Execution Predictions (BEFORE Running Code)

Before each cell, write answers in plain English:

What variables exist right now?

Which condition will Python check first?

Which condition will evaluate to True?

Which lines will be skipped?

✍️ Prediction Example:

“Python checks age < 18 first. Since age is 25, this is False.
It moves to age < 65, which is True, so it runs that block and ignores else.”

3️⃣ Trigger a Logic Error (On Purpose)

Create a wrong condition order:

age = 25

if age >= 0:
    print("Valid age")
elif age >= 18:
    print("Adult")


🧠 Prediction before running:

Will "Adult" ever print?

Why or why not?

4️⃣ Reorder the Code to Make It Work

Fix the logic without changing values:

age = 25

if age >= 18:
    print("Adult")
elif age >= 0:
    print("Valid age")


✍️ Explain:

What changed?

Why does order matter more than condition truth?

5️⃣ Explain Each Outcome in Plain English

For every run, answer:

Which condition was evaluated?

Which one stopped execution?

Which blocks were skipped?

Why indentation controls execution, not braces

**Planned Experiments**

Below is a **ready-to-run experiment pack** for your `sandbox.ipynb`, built **exactly** to your scope + intent.

**Rule:** For each cell → **PREDICT first (Markdown)**, then **RUN**.

---

## 🧪 EXPERIMENT PACK — CONDITIONAL LOGIC (if / elif / else)


---

## Experiment 1 — “ONLY ONE PATH RUNS”

### Cell 1 (Code)

```python
age = 25

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

print("Done")
```

**Predict (Markdown before running):**

* Which prints: Minor / Adult / Senior?
* Will `"Done"` print?

---

## Experiment 2 — “ORDER MATTERS MORE THAN CORRECTNESS” (Logic bug on purpose)

### Cell 2 (Code)

```python
age = 25

if age >= 0:
    print("Valid age")
elif age >= 18:
    print("Adult")
else:
    print("Invalid")
```

**Predict:**

* Will `"Adult"` ever print?
* Why does the first condition “block” the rest?

---

## Experiment 3 — Fix the logic by reordering (same values)

### Cell 3 (Code)

```python
age = 25

if age >= 18:
    print("Adult")
elif age >= 0:
    print("Valid age")
else:
    print("Invalid")
```

**Explain in plain English (Markdown):**

* What changed?
* Why does reorder fix it?

---

## Experiment 4 — Multiple conditions vs `elif` chain (difference in behavior)

### Cell 4 (Code)

```python
score = 92

print("Version A: separate ifs")
if score >= 50:
    print("Pass")
if score >= 90:
    print("Excellent")

print("\nVersion B: if/elif")
if score >= 50:
    print("Pass")
elif score >= 90:
    print("Excellent")
```

**Predict:**

* In Version A, how many lines print?
* In Version B, what prints and what gets skipped?

---

## Experiment 5 — Boolean expressions (`and`, `or`) with clear outcomes

### Cell 5 (Code)

```python
temp = 37.5
has_cough = True

if temp >= 38 and has_cough:
    print("Possible flu-like illness")
elif temp >= 38 or has_cough:
    print("Monitor symptoms")
else:
    print("Low concern")
```

**Predict:**

* Which branch runs?
* Which checks happen first?

---

## Experiment 6 — Short-circuit behavior (PROVE it with prints)

### Cell 6 (Code)

```python
def check(label, value):
    print("checked:", label)
    return value

print("Case 1: AND short-circuit")
if check("A", False) and check("B", True):
    print("AND: ran block")
else:
    print("AND: skipped block")

print("\nCase 2: OR short-circuit")
if check("C", True) or check("D", False):
    print("OR: ran block")
else:
    print("OR: skipped block")
```

**Predict (important):**

* In Case 1, will Python ever check **B**?
* In Case 2, will Python ever check **D**?
* Why?

---

## Experiment 7 — Indentation is execution control (what belongs to what)

### Cell 7 (Code)

```python
x = 3

if x > 0:
    print("A: inside if")
    print("B: inside if")
print("C: outside if")
```

**Predict:**

* Which lines are controlled by the `if`?
* What always prints no matter what?

---

## Experiment 8 — “Trap” logic: overlapping ranges (classic bug)

### Cell 8 (Code)

```python
n = 7

if n > 0:
    print("positive")
elif n > 5:
    print("greater than 5")
else:
    print("zero or negative")
```

**Predict:**

* Will `"greater than 5"` ever print for `n = 7`?
* What is the bug in the ordering?

---

## Experiment 9 — Fix the overlapping trap

### Cell 9 (Code)

```python
n = 7

if n > 5:
    print("greater than 5")
elif n > 0:
    print("positive")
else:
    print("zero or negative")
```

**Explain:**

* Why does this version work?

---

## Experiment 10 — Final “Execution Trace Challenge”

### Cell 10 (Code)

```python
age = 16
vip = True

if age >= 18 and vip:
    print("Entry: VIP adult")
elif age >= 18:
    print("Entry: adult")
elif vip:
    print("Entry: VIP minor (special)")
else:
    print("No entry")

print("End")
```

**Predict:**

1. Which conditions get evaluated? (in order)
2. Which one becomes True first?
3. What prints?
4. Which blocks are skipped?

---

# ✅ Your REQUIRED “Rules I Learned” (Paste into Markdown at end)

Copy this and fill it:

- Rule 1: Python checks conditions top-to-bottom, in the order they are written.

- Rule 2: Python runs only ONE branch in an if / elif / else block.

- Rule 3: elif is never checked if a previous if or elif evaluated to True.

- Rule 4: Order matters because Python stops at the first True condition, not the “best” or “most specific” one.

- Rule 5: and / or may skip checks because Python stops evaluating as soon as the final result is already known (short-circuit).

- Rule 6: Indentation decides which statements belong to which condition and therefore when they execute.

**One-line summary:**
Python doesn’t evaluate all conditions — it evaluates in order and commits to the first True path.

---

**Succes criteria:**
✔ I can explain how Python evaluates if / elif / else top-to-bottom
✔ I can predict which branch will run before execution
✔ I can explain why bad ordering causes logic bugs
✔ I recorded at least one reusable execution rule

--- 

