
# Daily Learning Log — Date: 2026-01-20

## Session Goals for Today
Understand how data moves through a sequence of Python steps, and how small, linear pipelines are built, broken, and fixed.

Not “advanced pipelines” — simple, visible, traceable flows.

**Focus topics:**
- Data flow through variables
- Step-by-step transformations
- Inputs → processing → outputs
- Mini pipelines (read → transform → produce)
- Where pipelines break when data is missing or out of order

**What I plan to do:**
Read concept note on Data Flow & Mini Pipelines

What a “pipeline” means in Python

Why order matters

How data is handed from one step to the next

2️⃣ Write execution predictions before running code
Before each cell, answer:

What data exists right now?

What variable holds it?

What will this line produce?

✍️ Prediction example (in plain English):

“At this point, age exists, but age_group does not.”

3️⃣ Build a tiny pipeline (intentionally fragile)
Example pattern (conceptual, not fancy):

raw_value → cleaned_value → computed_value → output


You will:

Start with raw input

Transform it step-by-step

Print at each stage

4️⃣ Break the pipeline on purpose

Use a variable before it receives data

Skip a transformation step

Reorder steps incorrectly

Observe:

NameError

Wrong output

Silent logic bugs (most dangerous)

5️⃣ Reorder steps to restore correct data flow

Move transformations earlier

Ensure each step receives valid input

Re-run and compare outcomes

6️⃣ Explain each outcome in plain English
For every run:

What data existed?

What data was missing?

Why Python behaved the way it did?

No jargon. Imagine explaining to a non-programmer.

**Planned Experiments**

Core "Fragile Pipeline" Drill

---

- Build a tiny pipeline (print every stage)

```python

print("=== FRAGILE PIPELINE (WORKING VERSION) ===")

raw_value = " 70 "                 # raw input (string with spaces)
print("Step 1 raw_value:", raw_value, type(raw_value))

cleaned_value = raw_value.strip()
print("Step 2 cleaned_value:", cleaned_value, type(cleaned_value))

number_value = int(cleaned_value)
print("Step 3 number_value:", number_value, type(number_value))

computed_value = number_value + 5
print("Step 4 computed_value:", computed_value, type(computed_value))

output = f"Result={computed_value}"
print("Step 5 output:", output, type(output))

```

---

- Break it: use before created (NameError)

```python

print("=== BREAK 1: USE BEFORE CREATED ===")

raw_value = " 70 "
print("raw_value:", raw_value)

# wrong order (number_value not created yet)
computed_value = number_value + 5
print("computed_value:", computed_value)

cleaned_value = raw_value.strip()
number_value = int(cleaned_value)

```

---

- Break it: skip a transformation (ValueError or TypeError)

```python

print("=== BREAK 2: SKIP TRANSFORMATION STEP ===")

raw_value = " 70 "
cleaned_value = raw_value.strip()

# skip int() conversion
computed_value = cleaned_value + 5     # should break: str + int
print("computed_value:", computed_value)

```

---

- Fix it: reorder steps to restore correct flow

```python

print("=== FIX: REORDER + ENSURE VALID INPUT ===")

raw_value = " 70 "
cleaned_value = raw_value.strip()
number_value = int(cleaned_value)
computed_value = number_value + 5
print("computed_value:", computed_value)

```

---

**Succes criteria:**
✔️ I can explain how data flows line-by-line through a mini pipeline
✔️ I can predict where a pipeline will break before running it
✔️ I can explain why reordering steps fixes the pipeline
✔️ I recorded at least one reusable data-flow rule

--- 

