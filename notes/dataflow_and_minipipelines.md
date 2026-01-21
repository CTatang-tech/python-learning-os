
---

# 📘 Day 5 Concept — Data Flow & Mini Pipelines

## Day 5 — Data Flow & Mini Pipelines

### One-Line Definition
A pipeline is a **sequence of steps** that transforms input into output.

---

### Why This Matters
Almost all real Python work is:
- Read data
- Clean data
- Transform data
- Output results

---

### Mental Model
Think:
**Input → Process → Output**

---

### Example Pipeline
1. Read CSV
2. Handle missing values
3. Compute summary
4. Write output

---

### Beginner Trap
Trying to be “clever” too early.

---

### Core Rules
- Start simple
- Make each step explicit
- Handle bad data early
- Data must exist BEFORE a step uses it (or NameError happens).
- Expressions produce VALUES; statements perform ACTIONS (assign/print/if/for/def/import).
- Order matters: pipelines are linear; each step depends on the previous step’s output.
- Type matters: wrong types cause TypeError OR silent logic bugs.
- Parentheses change evaluation order and can change results.
