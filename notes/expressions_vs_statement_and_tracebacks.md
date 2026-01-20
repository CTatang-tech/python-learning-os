
---

# 📘 Day 4 Concept — Expressions vs Statements & Tracebacks

## Day 4 — Expressions, Statements & Tracebacks

### One-Line Definitions
- **Expression:** produces a value
- **Statement:** performs an action

---

### Why This Matters
Understanding this explains:
- Why notebooks show values automatically
- Why some lines print and others don’t
- How to read errors correctly

---

### Examples
```python
2 + 2          # expression
print(2 + 2)  # statement
```
### Tracebacks Explained
A traceback tells you:
- Where Python was executing
- Where it failed
- What type of error occurred

### Mental Model

Tracebacks are a crime scene report, not an insult.

### Core Rules
- Expressions return values (you can store it, print it, or combine it).
- Statements control behavior (assign, loop, branch, define, import).
- Errors point to the real problem line
- SyntaxError happens before running (Python can’t parse your code)