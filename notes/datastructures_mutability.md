
## Week 4 Day 5 — Mutability & Structure Choice

### One-Line Definition
Mutability describes **whether data can change after creation**.

---

### Why This Matters
Mutability affects:
- bugs
- performance
- predictability
- safety

Wrong choices lead to subtle errors.

---

### Mental Model
- Mutable = editable whiteboard
- Immutable = printed document

---

### Mutability Summary
- list → mutable
- dict → mutable
- set → mutable
- tuple → immutable

---

### Decision Guide
Use:
- list → ordered collection
- tuple → fixed structure
- dict → named fields / records
- set → uniqueness & membership

---

### Beginner Traps
- Mutating shared data accidentally
- Using lists for records
- Ignoring immutability benefits

---

### Core Rules
- Mutability decides: update vs replace
- Choose structure based on intent
- Structure choice is a design decision
