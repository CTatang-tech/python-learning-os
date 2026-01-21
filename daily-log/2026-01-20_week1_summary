
## Python Execution Model

**Code as Sequence:** Python executes code line by line from top to bottom, but expressions within lines are evaluated before statements are fully executed.

**Expressions Produce Values:** Expressions (e.g., 2 + 3, len([1,2,3])) evaluate to a result; they are computed immediately when needed.
Statements Perform Actions: Statements (e.g., x = 5, print("hi"), if y > 5) execute actions like assignments or loops; they may not produce a reusable value.

**Evaluation Order:** Left-to-right for operators; precedence rules apply (e.g., * before +); function calls evaluate arguments first, then execute the function.

**Variable Binding:** Variables reference objects in memory; assignments create or update references, not containers.

## How Errors Arise

**Syntax Errors:** Malformed code (e.g., missing colon in if statement) prevents parsing; Python fails before execution.

**Name Errors:** Referencing undefined variables (e.g., print(user_score) before assignment) violates name resolution rules.

**Type Errors:** Operations on incompatible types (e.g., "12" + 3) assume types match; Python enforces type consistency at runtime.

**Execution Assumptions:** Code assumes correct order, types, and data sizes; violations trigger tracebacks during evaluation or action.

**Silent Failures:** Code runs but produces wrong output due to logic errors (e.g., incorrect precedence or unhandled edge cases).

## Reasoning About Failures

**Read Tracebacks Bottom-Up:** Start at the error line; trace the call stack to understand the failure path and violated assumptions.

**Identify Root Cause:** Check data types, execution order, and assumptions (e.g., "Did I confuse expression vs. statement?").

**Predict and Test:** Before running, predict values/types; after errors, manually fix and rerun to confirm.

**Common Mistakes:** Treating statements as values (e.g., print(x = 5)); ignoring precedence; assuming variables are containers.

**Prevention Rules:** Validate types early; use defensive checks; clarify expressions/statements in code structure.

## Data Flow and Mini Pipelines

**Linear Sequence:** Data moves through steps in order; each step transforms input to output (e.g., strip string → convert to int → compute).

**Dependencies:** Steps must run in sequence; using a variable before assignment causes NameError; skipping type conversion leads to TypeError.

**Fragile Nature:** Pipelines break if order is wrong (e.g., compute before convert) or types mismatch (e.g., string + int).

**Silent Breaks:** Wrong order or logic can run without errors but produce incorrect results (e.g., string comparison instead of numeric).

**Fixing Pipelines:** Reorder steps to ensure data exists and types match; add conversions (e.g., int()) to handle inputs properly.
