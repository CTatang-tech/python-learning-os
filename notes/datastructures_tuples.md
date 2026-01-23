## Week 4 Day 2 — Tuples (Fixed, Reliable Sequences)

### One-Line Definition
A tuple stores an **ordered collection of values that cannot change**.

---

### Why This Matters
Tuples are useful when:
- structure must not change
- data should be protected
- values represent a fixed record

They prevent accidental bugs.

---

### Mental Model
A tuple is a **sealed package**.
Once created, it cannot be opened or modified.

---

### Key Properties
- Ordered
- Immutable
- Allows duplicates

---

### Common Uses
- Coordinates (x, y)
- Function returns
- Fixed records

---

### What Python Is Doing Internally

1️⃣ Tuple creation is a one-time event

When execution reaches the tuple line, Python:

creates the tuple object

stores all element references inside it

binds the name to that object

Before that line runs, the tuple does not exist

Internally:

“I built this container once. I will not rebuild or edit it.”

2️⃣ Read operations are always allowed

Indexing and slicing are read-only

Python checks:

does the tuple exist now?

does this index exist now?

If the index is invalid → Python stops with an error

Internally:

“Reading is safe. Writing is forbidden.”

3️⃣ Write attempts are blocked immediately

Any attempt to:

replace an element

insert or remove elements

Python halts execution with an error

This is not a “style rule” — it is a hard execution rule enforced at runtime.

4️⃣ Rebinding vs mutating (the critical distinction)

Tuples cannot mutate

If a “change” appears to work, Python has:

created a new tuple

rebound the name to it

The old tuple remains unchanged in memory

Internally:

“I won’t edit this object. I’ll make a new one if you insist.”

5️⃣ The hidden gotcha: immutable container ≠ immutable contents

A tuple may contain mutable objects

Python protects the container, not what’s inside it

Inner mutable objects can still change

This is where many surprises come from.

---

### Beginner Traps
- Using tuples where updates are needed
- Confusing tuples with lists
- Trying to modify tuple elements:Python refuses immediately — no partial execution.
- Thinking immutability means ‘nothing inside can change’:Only the container is protected.
- Assuming += edits the tuple:It actually creates a new tuple and rebinds the name.

---

### Core Rules
- A tuple exists only after its creation line executes
- Tuples cannot change - names can: If something ‘changes,’ check whether Python replaced the object
- Use tuples for fixed structure
- Immutability = safety

### 🏁 One-Line Mental Model

A tuple is a sealed container created at runtime: Python can read from it forever, but it will never allow in-place edits — only replacement.