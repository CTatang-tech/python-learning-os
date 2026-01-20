
# Daily Learning Log — Day 1:2026-01-20

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
- Experiment 1: Expressions vs. Statements

Write 5 expressions (e.g., 2 + 3, "hello".upper()) and predict their values.
Write 5 statements (e.g., x = 5, print("hi")) and predict what they do (no output value).
Mix them in code and predict the overall behavior.

-Experiment 2: Triggering Tracebacks

Intentionally cause a NameError (e.g., reference undefined variable).
Cause a TypeError in an expression (e.g., invalid operation on types).
Cause a SyntaxError (e.g., malformed statement).
Analyze each traceback: What was Python trying to do? Where did it fail?

Experiment 3: Expression Evaluation Order

Predict the result of complex expressions (e.g., 5 + 3 * 2, function calls).
Use parentheses to change order and predict differences.
Test with variables: x = 10; y = x + 5; print(y).

Experiment 4: Statements in Sequence

Write a sequence of statements and predict the final state of variables.
Include assignments, prints, and conditionals (if simple).
Run and chec

Experiment 5: Debugging with Tracebacks

Write buggy code, run it, and use the traceback to fix it.
Focus on one error type per run (e.g., fix TypeError by casting).
Record: Original error, fix applied, lesson learned.

**Succes criteria:**
✔️ I can explain how data flows line-by-line through a mini pipeline
✔️ I can predict where a pipeline will break before running it
✔️ I can explain why reordering steps fixes the pipeline
✔️ I recorded at least one reusable data-flow ruled at least one reusable rule about expressions vs statement

--- 

