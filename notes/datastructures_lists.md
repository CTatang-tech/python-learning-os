
## Week 4 Day 1 — Lists (Ordered, Changeable Sequence)

### One-Line Definition
A list stores **an ordered collection of values** that can change.

---

### Why This Matters
Lists are used when:
- order matters
- items may change
- you need to loop over data

Most real-world datasets start life as lists.

---

### Mental Model
A list is a **row of boxes in a line**, numbered from left to right.

Indexing starts at **0**, not 1.

Most list bugs are timing bugs, not syntax bugs.

### What Python Is Doing Internally

1️⃣ List creation is an execution event

A list does not exist until Python executes its creation line

Before that moment, the name is unknown

After that moment, the name points to one list object in memory

Internally:

“I create the container now, not earlier.”

2️⃣ Index access is checked at the exact moment it runs

Python checks:

Does this list exist now?

Does this index exist now?

If the index is outside the current bounds → Python stops immediately

Internally:

“You asked for position n. I checked. It’s not there. I stop.”

No prediction. No forgiveness.

3️⃣ Mutation vs rebinding (the silent divider)

Mutation: the list object changes, the name stays

Rebinding: a new list is created, the name points elsewhere

This explains why:

Some changes are visible through multiple names

Other changes are not

The deciding factor is mutability, not the operator.

4️⃣ Lists grow over time — indexes appear only after elements are added

An index is not “reserved”

It exists only after the element is added

Accessing it too early always fails

Internally:

“I don’t care that you plan to add it later.”

---

### Key Properties
- Ordered
- Mutable (can change)
- Allows duplicates

---

### Common Uses
- Rows from a CSV
- Collections of values
- Iteration targets

---

### Beginner Traps
- Forgetting index starts at 0
- Modifying a list while looping
- Using lists for structured records
- Assuming a list or index exists before execution reaches it: Python only knows what has already run.
- Thinking list errors are about syntax: Most IndexErrors are order-of-execution problems.
- Forgetting that lists are mutable: Multiple names can point to the same list, so changes “leak”.

---

### Core Rules
- Lists preserve order
- Lists can grow and shrink
- Use lists for collections, not records
- A list exists only after its creation line executes
- An index exists only after the element is added
- If behavior surprises you, check: did Python update the object or replace it?

### One-Line Mental Model

A list is a live container in memory that Python checks moment-by-moment; order and timing decide whether an operation succeeds or crashes.