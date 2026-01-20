## Explicitly Forbidden AI Roles (Week 1)

**AI must never:**
- Predict output before the human
- Explain code the human hasn’t tried to explain
- Fix code unless explicitly asked after diagnosis
- Teach syntax proactively
- Summarize concepts the human hasn’t encountered

If any of these happen, Week 1 integrity is broken.

**Gold-Standard Evidence AI Was Used Correctly**

At the end of Week 1, artifacts should show:
- Raw AI-generated broken code
- Human predictions written before execution
- Human explanations written before AI explanations
- AI explanations that reference execution order
- Human-authored fixes

If the notebook reads like a tutorial, it’s wrong.
If it reads like a lab notebook, it’s right.

## Generate Examples (Controlled Input Generator)
- Purpose
- AI exists to produce raw material for human reasoning, not solutions.
- If AI produces answers, it has failed its role.

--

***Gold-Standard Use Case A(Generate Broken Code for Debugging)***

Generate a short Python example (5–10 lines max) that contains:
- 2–3 beginner mistakes
- at least one type-related error
- at least one variable or indexing error

Do NOT explain the errors.
Do NOT fix the code.
Only output Python code.

---

This trains:
Traceback reading
Locating failure point
Understanding evaluation order

---

***Gold-Standard Use Case B(Generate Prediction Challenges)***

Generate a short Python code snippet where:
- the output is non-obvious to beginners
- variables are reassigned
- no syntax errors occur

Do NOT explain the output.

---

***Gold-Standard Use Case C(Generate “Near-Miss” Code)***

Code that almost works, but fails late.

Generate Python code that:
- runs for several lines
- then fails with a runtime error
- error should involve types or indexing

Do NOT explain or fix it.

---

This trains:
Traceback reading
Locating failure point
Understanding evaluation order

## Explain Memory & Execution (Post-Attempt Only)**
AI explanations are retrospective, never anticipatory

Gold-Standard Rule (Non-Negotiable)

Human explanation must exist in writing before AI is queried.

If the human explanation is missing, AI must not be used.

***Gold-Standard Use Case D (evaluationg an expression)***
Explain How Python Evaluated an Expression
Human Writes First (Required)

Example:

Python tried to evaluate age + 1.
age is a string, 1 is an integer.
The + operator is not defined for these types together.

---

Explain step by step how Python evaluated this code.
Include:
- order of execution
- types involved at each step
- where execution stopped and why

---

Gold-Standard AI Output Characteristics
AI explanation must:
- Follow Python’s execution order
- Name exact types
- Describe why Python refuses, not just that it does
- Avoid human metaphors unless clarifying (no “Python gets confused”)

Forbidden AI Behavior
- Jumping directly to the fix
- Rewriting the code
- Explaining without referencing execution order
- Using vague phrasing like:
- “Python doesn’t like this”
- “This causes an error because it’s wrong”

---

***Gold-Standard Use Case E(Explain Variable Assignment & References)***
Human Question (After Attempt)

I expected y to change when x changed, but it didn’t.
Explain how Python handles variable assignment here.

AI Must Explain Using:
- “name → object” model
- Assignment vs mutation
- Rebinding vs modifying

---

Acceptable Explanation Pattern
y = x binds y to the same object x refers to at that moment. When x is reassigned, y is unaffected because it still refers to the original object.

## Validate (Not Replace) Human Reasoning
AI acts as a logic checker, not a teacher.

***Gold-Standard Use Case F(Reasoning Validation)***

Human Writes

- The error is an Index Error because index 3 does not exist.
- The list length is 3, valid indices are 0–2.

---

Allowed AI Prompt
- Check whether my explanation of this error is accurate.
- If anything is incomplete or imprecise, point it out.
- Do not re-explain from scratch.

---

Gold-Standard AI Response
- Confirms correctness
- Adds missing precision (if any)
- Does not overwrite human explanation