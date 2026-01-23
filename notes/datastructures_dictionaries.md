## Week 4 Day 3 — Dictionaries

### One-Line Definition
A dictionary stores **data as key–value pairs**.

---

### Why This Matters
Dictionaries are the backbone of:
- records
- JSON data
- APIs
- real-world entities

Almost all structured data maps naturally to dicts.

---

### Mental Model
A dictionary is a **labeled filing cabinet**.
You retrieve values by **name**, not position.

---

### Key Properties
- Unordered (conceptually)
- Mutable
- Keys must be unique

---

### Common Uses
- User records
- Configuration
- Parsed JSON

---

### Beginner Traps
- Assuming order matters
- Accessing missing keys directly
- Using lists instead of dicts for records

---

### Core Rules
- Keys identify values
- Dicts model real-world objects
- Use `.get()` when keys may be missing
