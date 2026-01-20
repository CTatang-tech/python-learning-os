## Standard AI Prompt Block (Embed in Every Note)

## 🤖 AI Prompt Toolkit (Reusable)

Copy-paste one at a time:

- Explain this concept using a real-world analogy.
- Explain this as if teaching a smart 12-year-old.
- Generate 3 beginner mistakes and explain why they fail.
- Produce a broken example and ask me to debug it.
- Explain what happens in memory step-by-step.
- Turn this into a multiple-choice trick question.
- Ask me a “predict the output” question.
- Summarize this in 3 rules.

## AI Task 1 — Generate learning summaries
When to use
•	End of a study session
•	After finishing a lesson/video/article
•	After debugging something painful
•	Weekly “what did I learn?” review

**Gold-standard workflow (every time)**

Step 1 — Paste “raw learning signals”

**Give the AI inputs, not vibes. Paste any of:**
•	your notes (even messy)
•	code snippets you wrote
•	error tracebacks you hit
•	what concept you just studied
•	what confused you

**Step 2 — Ask for a structured summary**
Use this exact template:

Prompt (copy/paste):

Summarize what I learned today using this structure:
Concepts (3–7 bullets)
“I can now do…” (3 bullets)
Mistakes I made + fixes (2–5 bullets)
One mini-exercise to prove I learned it
Flashcards: 6 Q→A pairs
Keep it beginner-friendly and concrete.


**Step 3 — Turn it into “Rules I learned”**
Immediately follow with:

Extract 5 “Rules I learned” from that summary (simple, testable rules).
Each rule must include a tiny example.

**Step 4 — Save it**
Paste the output into:
•	00_SUMMARIES.md (date heading)
•	your notebook “Rules I learned” section

**Step 5 — The “tomorrow plan”**
End with:

Based on today’s summary, propose the next 3 micro-topics I should learn in the correct order, and 1 debugging drill.

## AI Task 2 — Explain unfamiliar terms
When to use
•	You see a term you can’t explain in 1 sentence
•	Docs/tutorials use jargon
•	You hit an error message you don’t understand
Gold-standard workflow (every time)

**Step 1 — Capture the term in context**
Give the AI:
•	the term
•	the sentence/code where it appeared
•	what you think it means (even if wrong)

Prompt (copy/paste):

Explain the term “___” in the context below.
Context: [paste sentence/code]
My current guess: [your guess]
Teach it in 3 layers:

one-sentence definition (kid-simple)
practical meaning in Python (what it changes/affects)
tiny example + “what would go wrong if misunderstood”

**Step 2 — Force a “contrast explanation”**
This is where understanding locks in:

Contrast “___” with the closest confusing neighbor term (e.g., expression vs statement, list vs tuple, function vs method). Use a 2-column comparison.

**Step 3 — Add to your glossary**
In 00_GLOSSARY.md, save:

•	Term:
•	Plain definition:
•	Why it matters:
•	Example:
•	Common confusion:

**Step 4 — Quick check**
To verify you actually got it:

Quiz me with 5 quick questions (mixed true/false + tiny code predictions) about this term.

## Expressions vs Statements

**Core Tutor Prompt**

Explain which parts of this code are expressions and which are statements.
For each expression:
- what value it evaluates to
- when that value exists

For each statement:
- what action Python takes
- whether it produces a value

**Execution Flow Prompt**

Walk through how Python executes this code from top to bottom.
Explain:
- when expressions are evaluated
- when statements are executed
- how this affects variable assignment

**Common Error Prompt**

Show a beginner mistake caused by confusing expressions and statements.
Explain:
- what the programmer expected
- what Python actually did
- why the misunderstanding occurred

**Refactoring Insight Prompt**

Rewrite this code to make the distinction between expressions and statements clearer.
Do not change behavior