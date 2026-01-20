## Day 1 — Python Execution Model

### One-Line Definition
Python executes code **top to bottom**, one statement at a time.

---

### Why This Matters
If you don’t understand execution order:
- Errors feel random
- Debugging feels like guessing
- Notebooks silently lie to you

---

### Mental Model
Think of Python as a **reader**:
- It reads your file from the first line
- Executes each line immediately
- Stops completely if it hits an error

Python does **not**:
- Look ahead
- Remember future code
- Guess your intention

---

### Key Distinctions
- **Script (.py):** runs top → bottom once, stops at first error
- **Notebook (.ipynb):** cells can run out of order (dangerous), state persists between runs, can create false **confidence** (misleading if i'm careless)

---

### Beginner Mistake
Thinking Python “knows what you mean” later in the file.

```python
print(x)   
x = 10
```
**What the developer thought:**
“Python will see x later.”
**What Python actually does:**
Tries to print x before it exists → NameError

---

### How Python Exexcutes This 
- Starts at the first line
- Executes immediately
- Fails if a name is unknown
- Stops execution on error
- Never reaches later lines

---

### Micro-Tests (predict before running)
```python
print("Start")
print(y)
y = 5
print("End")

x = 10
print(x)
x = x + 1
print(x)
```

---

### Core Rule
Python does NOT look ahead. It only knows what has already executed.

---

### Related Concepts
- [[variables_and_type]]
- [[errors_and_tracebacks]] 

---

### AI Prompt Hooks
- Explain Python execution using a real-world analogy
- Generate 3 execution-order mistakes beginners make
- Create a notebook-specific execution trap
- Explain why NameError happens step-by-step

---