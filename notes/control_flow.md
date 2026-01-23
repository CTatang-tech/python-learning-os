

---

# 📘 Day 2 — Conditional Logic (or Control Flow) (`if / elif / else`) 

```md
## Week 1 Day 2 — Conditional Logic

### One-Line Definition
Conditional statements let Python **choose what code to run** based on conditions.

---

### Why This Matters
Without conditionals:
- Programs can’t adapt
- All logic is linear
- Real-world decisions are impossible

---

### Structure
```python
if condition:
    action
elif another_condition:
    action
else:
    fallback
```
## Mental Model

Think of if as a fork in the road.
Only ONE path is taken.

or 

Think of an if / elif / else chain as a single decision gate, not multiple questions.

Python asks: “Is this True?”
If yes → commit and stop
If no → move to the next question
There is no backtracking
Only ONE path can ever run.


## What Happens Internally (Step-by-Step)

Each condition is a boolean expression that must resolve to True or False

Expressions are evaluated, then the result is used to decide execution

Boolean operators (and, or) may short-circuit, meaning: Parts of a condition may never be evaluated at all

Indentation defines which statements are controlled by the condition

Once Python exits the conditional block, execution resumes normally


## Common Errors

- Forgetting indentation
- Using = instead of ==
- Overlapping conditions
- Wrong ordering of conditions: Broad conditions placed before specific ones make later branches unreachable.
- Assuming Python checks all conditions: It doesn’t. Python stops at the first True.
- Forgetting short-circuit behavior: With and / or, Python may skip evaluating entire expressions, so expected checks or side effects never occur.

## Core Rules

- Conditions must evaluate to True or False
- Indentation defines logic blocks
- Python stops checking once a condition is met
- Order defines meaning: Python chooses the first True condition, not the best one.
- Only one branch ever runs: if / elif / else is a single decision, not multiple independent tests.
