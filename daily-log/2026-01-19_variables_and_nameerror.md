
# Daily Learning Log — Day 2:2026-01-19

## Session Goals for Today
Understand what a variable is, when it comes into existence, and why Python raises a NameError when you use one too early.

**Focus topics:**
- Variables
- Name binding (when a variable is created)
- NameError as an execution-time error
- Top-to-bottom execution

**What I plan to do:**
- Read concept note on Variables & NameError in Python
- Write execution predictions before running each cell
- Trigger a NameError by using a variable before definition
- Reorder code to make it work
- Explain each outcome in plain English

**Succes criteria:**
- I can explain how Python moves line by line through code
- I can predict when a NameError will occur before execution
- I can explain why reordering lines fixes errors
- I recorded at least one reusable execution rule

--- 

##  Accomplishments
- Concepts Studied (Reflected in notes/)

- Core Concept: Variables and NameError

- Key Insight 1:
A variable is not a box—it is a name (label) that points to a value in memory.

- Key Insight 2:
The = operator means assignment, not “equals”; Python evaluates the right-hand side first, then binds the name on the left.

- Additional understanding gained:

Variables must be assigned before use

Reassignment changes the binding, not the value itself

Errors feel less “mysterious” once execution order is understood

## Tasks Completed (Reflected in sandbox.ipynb)

- Created a structured sandbox notebook session header (goal, questions, predictions)

- Ran multiple micro-test cells using simple assignments (x = 5, y = x + 2)

- Practiced prediction → execution → explanation workflow for each cell

- Documented observations in plain English after execution

## Challenges & Blockers

- Problem Encountered:
Initial tendency to think of = as a mathematical equality instead of assignment.

- Resolution / Lesson Learned:
Always read = as “is assigned to” and trace execution top-to-bottom.

- Next Steps on Blockers:
Reinforce this mental model when moving to expressions, types, and reassignment.

## Time & Metrics

Total Focused Learning Time: ~1.5 hours

Project Code / Testing Time: ~1 hour

Energy Level (1–5): 4

## Rules I learned 

- A variable must be assigned before it can be used; otherwise, a NameError occurs.

- Always read = as “is assigned to”

## Plan for Tomorrow (2025-12-18)

High Priority Task 1:
Extend sandbox to types (int, float, str, bool) and observe how variables bind to different object types.

High Priority Task 2:
Introduce intentional errors (e.g., using undefined variables) and practice reading tracebacks calmly.