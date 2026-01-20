
# Daily Learning Log — Day 1:2026-01-19

## Session Goals for Today
Undertsand when does Python “produce a value” vs “perform an action”?

**Focus topics:**
- What an expression is in Python
- What a statement is in Python
- How Python evaluates expressions
- How Python executes statements
- Why some lines can be printed and others cannot

**What I plan to do:**
- Read concept note on expressions vs statements

Learn the definition difference

Identify which parts of code return a value

2️⃣ Write predictions before running each cell
Before executing, answer:

“Will this line produce a value?”

“Will this line just do something?”

3️⃣ Test pure expressions

Arithmetic (2 + 3)

Comparisons (5 > 3)

Function calls that return values (len("hi"))

4️⃣ Test statements

Assignment (x = 5)

Import (import math)

Control flow (if, for, while)

5️⃣ Trigger common confusion cases

Try to print(x = 5) → observe failure

Try a bare expression vs print(expression)

Compare x + 1 vs x = x + 1

6️⃣ Explain each outcome in plain English

Why some lines “show a value” in the notebook

Why others don’t show anything unless printed

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
✔ I can explain what an expression is in simple words
✔ I can explain what a statement is in simple words
✔ I can predict whether a line produces a value or not
✔ I understand why print(2 + 3) works but print(x = 5) does not
✔ I recorded at least one reusable rule about expressions vs statement

--- 

