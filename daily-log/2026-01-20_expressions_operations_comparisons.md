
# Daily Learning Log — Date:2026-01-19

## EXPRESSIONS, OPERATIONS & COMPARISONS

## Session Goals for Today
Understand how Python evaluates expressions, performs operations, and makes comparisons — step by step, top to bottom, without guessing.

By the end of this session, you should see how Python turns symbols into values.

**Focus topics:**
- What an expression is (vs a statement)
- How operations are evaluated
- Operator precedence (what runs first)
- Comparison expressions (==, <, >, etc.)
- Why expressions can succeed or fail depending on types

**What I plan to do:**
1️⃣ Read Concept Note

Topic: Expressions, Operations & Comparisons

Focus on:

“An expression produces a value”

Python evaluates right now, not later

Operators don’t work on everything

Mental checkpoint:
“If I run this line, what VALUE does it produce?”

2️⃣ Write Execution Predictions Before Running Code

Before every cell, answer in plain English:

What values exist right now?

What types are they?

What operation is Python about to attempt?

Will this line produce:

a value?

True / False?

an error?

✍️ Prediction examples:

“This expression will evaluate to 7.”

“Python will try to add a string and an integer → TypeError.”

“This comparison will return False.”

3️⃣ Trigger Errors on Purpose (Learning Traps)

You will intentionally break expressions to understand rules.

Examples of traps:

Mixing incompatible types

Assuming Python “converts automatically”

Comparing values you think are equal

Your job is not to fix immediately, but to explain:

“What was Python trying to do here?”

4️⃣ Reorder or Rewrite Expressions to Make Them Work

You will:

Add parentheses

Change operation order

Convert types explicitly 

Then explain why the new version works.

5️⃣ Explain Every Outcome in Plain English

For each line, complete this sentence: 

“Python evaluates this expression by first ___, then ___, resulting in ___.”

If you can’t say it out loud → you don’t understand it yet.

**Planned Experiments**

Below is a **ready-to-run experiment pack** you can paste straight into `sandbox.ipynb` (cell by cell). It’s built to match your scope: **predict → run → explain**.

> **RULE:** Do NOT run a cell until you fill the **PREDICTION** block.

---

## ✅ SANDBOX EXPERIMENT PACK — Expressions, Operations & Comparisons

---

# EXPERIMENT 1 — Expressions produce VALUES

## Cell 2 — Five expressions (predict values)

```python
# PREDICTION (write BEFORE running):
# 1) 2 + 3 -> ?
# 2) "hello".upper() -> ?
# 3) len([1,2,3,4]) -> ?
# 4) 3 > 10 -> ?
# 5) (10 // 3) + (10 % 3) -> ?

print("2 + 3", 2 + 3)
print('"hello".upper()', "hello".upper())
print("len([1,2,3,4])", len([1, 2, 3, 4]))
print("3 > 10", 3 > 10)
print("(10 // 3) + (10 % 3)", (10 // 3) + (10 % 3))
```

✅ **Explain after running (write in Markdown):**
“Python evaluates this expression by first ___, then ___, resulting in ___.”

---

# EXPERIMENT 2 — Statements do ACTIONS (often no value you keep)

## Cell 3 — Five statements (predict what happens)

```python
# PREDICTION (write BEFORE running):
# What prints? What variables exist after?

x = 5
print("hi")
y = x + 2

if y > 5:
    print("y is big")

for i in range(2):
    print("loop", i)

print("x =", x)
print("y =", y)
```

✅ **Checkpoint:** Which lines were **statements**? Which ones **produced values**?

---

# EXPERIMENT 3 — Operations depend on TYPES

## Cell 4 — Same operator, different types (predict outcomes)

```python
# PREDICTION:
# Which lines succeed? Which fail? Why?

print("'a' + 'b'", 'a' + 'b')
print("3 + 4", 3 + 4)
print("[1,2] + [3]", [1, 2] + [3])

print("'ha' * 3", "ha" * 3)
print("[9] * 4", [9] * 4)
print("10 / 4", 10 / 4)
print("10 // 4", 10 // 4)
print("10 % 4", 10 % 4)
```

✅ **Explain:** “Operator ___ means ___ for type ___.”

---

# EXPERIMENT 4 — Operator precedence (what runs first)

## Cell 5 — Precedence tests (predict results)

```python
# PREDICTION:
# 1) 5 + 3 * 2 = ?
# 2) (5 + 3) * 2 = ?
# 3) 10 - 4 / 2 = ?
# 4) (10 - 4) / 2 = ?

print("5 + 3 * 2", 5 + 3 * 2)
print("(5 + 3) * 2", (5 + 3) * 2)
print("10 - 4 / 2", 10 - 4 / 2)
print("(10 - 4) / 2", (10 - 4) / 2)
```

✅ **Say out loud:** “Python does * before + unless parentheses override it.”

---

# EXPERIMENT 5 — Comparisons produce True/False (and can surprise you)

## Cell 6 — Comparison basics (predict True/False)

```python
# PREDICTION: True or False for each?

print("3 == 3", 3 == 3)
print("3 == '3'", 3 == "3")
print("3 < 10", 3 < 10)
print("'a' < 'b'", "a" < "b")
print("5 <= 5", 5 <= 5)
print("5 != 5", 5 != 5)
```

✅ **Explain:** Why is `3 == "3"` not True?

---

## Cell 7 — Chained comparisons (predict)

```python
# PREDICTION:
# What does this evaluate to, and why?

print("1 < 2 < 3", 1 < 2 < 3)
print("1 < 2 > 3", 1 < 2 > 3)
print("5 == 5 == 5", 5 == 5 == 5)
```

✅ **Rule:** Python can chain comparisons in one expression.

---

# EXPERIMENT 6 — Learning traps (intentional errors)

## Cell 8 — NameError trap (run it and read traceback)

```python
# PREDICTION:
# What is Python trying to do? Where will it fail? What error?

print(score)
score = 10
```

---

## Cell 9 — TypeError trap (run it and read traceback)

```python
# PREDICTION:
# What operation is attempted? Why does it fail?

age = "12"
print(age + 3)
```

---

## Cell 10 — SyntaxError trap (DO NOT FIX FIRST — run to see it)

```python
# PREDICTION:
# Why does Python refuse to start? What is malformed?

if 3 > 2
    print("yes")
```

---

# EXPERIMENT 7 — Rewrite to make it work (fix AFTER understanding)

## Cell 11 — Fix NameError by reordering

```python
# PREDICTION:
# Why will this version work?

score = 10
print(score)
```

---

## Cell 12 — Fix TypeError by converting type

```python
# PREDICTION:
# What will print now?

age = "12"
print(int(age) + 3)
```

---

## Cell 13 — Fix SyntaxError by correct syntax

```python
# PREDICTION:
# What prints now?

if 3 > 2:
    print("yes")
```

---

# EXPERIMENT 8 — Full “Explain Every Outcome” drill

## Cell 14 — One-line narration challenge

```python
# BEFORE running, narrate line-by-line:
# “Python evaluates ___ first, then ___, resulting in ___.”

x = "5"
y = 2

# Try to predict: does this work?
# Uncomment ONE at a time after predicting.

# print(x + y)
# print(int(x) + y)
# print(x * y)
# print(str(y) + x)
```

---

## Your hard “Success Criteria” check (quick)

When you finish, you should be able to say:

1. **Expression produces a value.**
2. **Statements perform actions.**
3. **Operators depend on types.**
4. **Precedence decides order unless parentheses override.**
5. **Comparisons return True/False — but types matter.**


**Succes criteria:**
✅ I can explain what an expression is (in one sentence)
✅ I can predict the result of an operation before running it
✅ I can explain why a comparison is True or False
✅ I can predict TypeError vs valid result
✅ I recorded at least one reusable rule

--- 

