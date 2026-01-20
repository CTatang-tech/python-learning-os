

# Week 0 -🧠 AI Tasks Prompts - Gold Standard Specification(Python Foundations Weeks 1-3)

Principle: AI explains after you think, and critiques after code runs 

Prime Directive:
AI proposes. You judge. You decide.

One-Sentence Takeaway:
AI is your junior developer and debugging partner — never your architect or decision-maker.

## Full AI Role Stack (Integrated View)

| AI Role          | When Used             | Output Type                    |
| ---------------- | --------------------- | ------------------------------ |
| Junior Developer | After problem framing | First-draft code               |
| Tutor            | After running code    | Execution explanation          |
| Debugger         | After failure         | Root-cause analysis            |
| Reviewer         | After success         | Readability & quality critique |
| Tester           | After review          | Edge cases                     |
| Summarizer       | End of session        | Mental models                  |
| Terminologist    | When confused         | Runtime explanations           |


### Correct Role Invocation Order (Very Important) 

Problem Framing (human)
→ First Attempt (human)
→ Junior Developer (AI)
→ Tutor (AI)
→ Debugger (AI, if needed)
→ Reviewer (AI)
→ Tester (AI)
→ Summary (AI)
→ Reflection (human)

### Example: Gold-Standard Day (Concrete)

Problem:
“Add two numbers provided as strings.”

Your attempt → error

Debugger Prompt Used:
Analyze this traceback.
Explain what Python was trying to do and why it failed.

Junior Dev Prompt (after understanding):
Act as a junior Python developer.
Write the simplest readable solution.
List assumptions.

Reviewer Prompt:
Review for clarity and edge cases.

Each role is used once, intentionally.

### Minimal Prompt Set (Final, Save These 10)

If you save only one page, save this:

Junior dev – readable first draft
Minimal working example
Tutor – execution explanation
Debugger – traceback analysis
Debugger – root-cause mental model
Reviewer – clarity & correctness
Tester – edge cases
Learning summary
Teach-back summary
Term explanation

These 10 prompts cover Weeks 1–3 fully and scale to professional work.

## Learning Summaries and Unfamiliar Terms

Good learning summaries and term explanations describe how Python behaves at runtime and why misunderstandings cause errors — not just what words mean.

### How to Use These Prompts Correctly (Critical)

✅ Correct Workflow
- You encounter a term you don’t fully understand
- You write your guess of what it means
- You use one of the prompts in the section for summaries and unfamiliar terms
- You rewrite the explanation in your own words

❌ Incorrect Workflow
- Copying definitions
- Letting AI explain everything first
- Treating summaries as “notes to memorize”

Example: Gold-Standard Use (Concrete)

Term: Traceback
Your guess (human first):
“It’s Python telling me where something broke.”

AI Prompt Used: 

Explain the term ‘traceback’ in plain language.
Include runtime behavior, analogy, misconception, and example.

What You Extract (not copy):
Tracebacks show the path Python took
Last line is the failure
Read bottom → top
You then write your own version in notes.

###  AI Task: Generate Learning Summaries
#### 🎯 Purpose
Turn raw practice into conceptual understanding and transferable rules, not notes to memorize
#### ✅ Human Responsibility
- Read summary critically
- Rewrite key points in your own words
- Reject anything you don’t understand
#### 🧑‍🏫 Core Learning Summary Prompt
* Use this at the end of a study session or day

Generate a concise learning summary of today’s Python concepts.
Constraints:
- Focus on execution and mental models, not syntax
- Explain what Python is doing internally
- Include 3 common beginner mistakes
- Include 3 rules of thumb I should remember
- Do NOT include code unless necessary
####  🧠 “Teach-Back” Summary Prompt (very important)
* Use this to test understanding

Summarize today’s Python concepts as if I must explain them to a non-programmer.
Avoid jargon.
If jargon is unavoidable, define it immediately.
####  🔍 Diagnostic Summary Prompt
* Use this when something felt confusing

Based on today’s topic, what are the most likely misconceptions a learner like me would have?
Explain why each misconception is tempting and how to correct it.
####  One-Page Summary Prompt (Weekly Use)

Create a one-page conceptual summary of the following Python topics.
Focus on:
- how Python executes code
- how errors arise
- how to reason about failures
Use short sections and bullet points

### AI Task: Explain Unfamiliar Terms (Gold-Standard Prompt)
#### 🎯 Purpose
Replace dictionary definitions with runtime intuition

#### ✅ Human Responsibility
- Write your own explanation first
- Use AI only to refine or correct
- Add the term to your personal notes, not copied text

#### 📖Core Term Explanation Prompt (Never Use Dictionary Style)

Explain the following Python term in plain language.
Include:
- what it means in practice
- why it exists
- one real-world analogy
- one common beginner misunderstanding
- one tiny Python example

#### 🧠 Mental-Model-First Term Prompt
* Use this when a term feels abstract

Explain this term by focusing on how Python behaves at runtime.
Avoid formal definitions first.
Explain what Python is actually doing.

#### 🔄 Contrast Prompt (Very Powerful)
* Use when terms are easily confuse

Explain the difference between these two Python terms.
For each:
- what Python does internally
- when beginners confuse them
- how to tell which one is happening in code

* Example uses: 
- expression vs statement
- variable vs value
- name vs object

#### ⚠️ “Why This Matters” Prompt

Why does this Python term matter in real code?
Explain:
- what bugs occur if I misunderstand it
- how it shows up in tracebacks
- how professionals think about it

## AI Task: Act as (Junior Developer) then (Tutor) then (Debugger) then (Reviewer) then (Tester) 

### How to use these prompts correctly (critical)

✅ You:
- Predict behavior
- Run code
- Interpret result or error
- THEN use AI

❌ You never:
- Ask AI before thinking
- Copy explanations verbatim
- Skip reviewing AI output

### 1️⃣ AI as Junior Developer (Code Generation)
#### 🎯 Purpose
Produce first-draft, readable code that you can audit, modify, and improve — never final solutions

❌ What You Never Ask as Junior Dev: 
“Write production-ready code”
“Optimize this”
“Use advanced Python tricks”

✅ Human Responsibilities (Non-Negotiable)
Compare AI code with your own attempt
Identify incorrect assumptions
Rewrite at least one part manually
Reject code you don’t understand

#### ✅ Primary Junior Developer Prompt
Use after you define the problem in plain English

Act as a junior Python developer.

Write a simple, readable solution to the following problem.
Constraints:
- prioritize clarity over cleverness
- use basic Python only
- do not optimize
- add comments explaining intent
- list assumptions you are making

Problem:
[PASTE YOUR PROBLEM STATEMENT]

#### 🧠 Minimal Working Example Prompt
Use when you want the smallest possible solution.

Generate a minimal working Python example that demonstrates
how to solve this problem.
Explain what this example does and what it does NOT handle.

#### 🔄 Refactor-Later Guardrail Prompt
Use to prevent premature optimization.

Write the most straightforward version of this code.
We will refactor later.
Do not use advanced Python features.


### 🧑‍🏫 AI as Tutor (Understanding & Execution)
* When to Use
- After code runs
- After you predict behavior
- After you attempt explanation

#### ✅Tutor prompt

Explain this Python code line by line.
Include:
- execution order
- data types created
- how variables reference objects
- what would break if a line were removed

#### 🧠 Deep-Reasoning Tutor Prompt

Explain why this code works, not just what it does.
Include the assumptions Python is making.

### AI as Debugger (Error Diagnosis)
#### 🎯 Purpose
Turn errors into learning opportunities, not quick fixes.

✅ Human Responsibilities (Critical)
Always interpret error first
Apply fix manually
Rerun and confirm behavior
Record the lesson learned

#### ✅ Primary Debugger Prompt (Traceback Analysis)
Use after you read the traceback yourself.

Analyze this Python traceback.
Explain:
what Python was trying to do
where execution failed
which assumption was violated
why this specific error type was raised
how to fix it
how to prevent it in the future

#### 🧠 Root-Cause Analysis Prompt
Use when the error is subtle or recurring.

Identify the root cause of this bug.
Explain:
- the incorrect mental model behind it
- why a beginner would make this mistake
- how to update the mental model to avoid it

#### 🐞 Silent Failure Prompt
Use when code runs but output is wrong.

This code runs without errors but produces incorrect output.
Explain:
what assumptions are incorrect
where logic deviates from intent
how to detect this kind of bug earlier

#### 🔁 Prevention-Focused Debugger Prompt

Show two defensive programming techniques
that would prevent this error.
Explain the trade-offs of each.

 
### 🔍 AI Task: Reviewer (After Code Works)
When to Use:
Code runs successfully
Basic correctness confirmed

#### ✅ Human Responsibility

Accept only changes you fully understand
Reject “clever” code that reduces clarity
Apply changes manually

#### ✅ Reviewer Prompt (code quality)
 
Review this Python code for:
readability
correctness
edge cases
Pythonic style

Suggest improvements and explain why each change helps.
Do not optimize for cleverness

#### 🧪 Reviewer-as-Tester Prompt (robustness)

What inputs or situations would cause this code to fail
or produce misleading results?
List at least 5 edge cases.









# Week 1 - Python Execution & Mental Models

* Rule: These prompts are only used after I have predicted behavior, run the code, and written my own explanation

## Variables & Types

## # Core Tutor Prompt

Explain how Python handles variables and types in this code.
Include:
- what objects are created
- what names (variables) reference
- how memory references change line by line
- why Python does not treat variables as containers
Use a concrete example from the code.

## # Deep Understanding Prompt

Explain the difference between a variable name and the object it refers to.
Use:
- one correct example
- one common beginner misconception
- one example that causes unexpected behavior


## # Type Awareness Prompt

For each variable in this code:
- state its type
- explain how Python determined that type
- say whether the type could change later
- give one operation that would fail for this type and why


## # Mental Model Validation Prompt

If I change the order of these lines, how does Python’s behavior change?
Explain the execution step by step.


## Expressions vs Statements

## # Core Tutor Prompt

Explain which parts of this code are expressions and which are statements.
For each expression:
- what value it evaluates to
- when that value exists
For each statement:
- what action Python takes
- whether it produces a value

## # Execution Flow Prompt

Walk through how Python executes this code from top to bottom.
Explain:
- when expressions are evaluated
- when statements are executed
- how this affects variable assignment

## # Common Error Prompt

Show a beginner mistake caused by confusing expressions and statements.
Explain:
- what the programmer expected
- what Python actually did
- why the misunderstanding occurred

## # Refactoring Insight Prompt

Rewrite this code to make the distinction between expressions and statements clearer.
Do not change behavior.
Explain why the new version is easier to reason about.

## Tracebacks

## # Core Traceback Tutor Prompt

Explain this Python traceback step by step.
Include:
- which line failed
- what Python was trying to do
- what assumptions failed
- how Python decided to raise this error

## # Reading Strategy Prompt (critical)

Explain how to read this traceback from bottom to top.
For each line, explain what information it provides and why it matters.

## # Failure Cause Prompt

What incorrect assumptions does this code make about:
- data types
- data structure size
- execution order
Explain how those assumptions led to the error.

## # Prevention-the-bug Prompt

How could this error have been prevented?
Provide:
- one defensive programming technique
- one validation check
- one design change
Explain the trade-offs of each.

