

## 🧠 Session Goals for Today

**Concept Topic:** Data Structures — **Sets(uniqueness & membership)**

**Big Goal:**
Understand **what a set is**, **why it exists**, and **how Python executes set operations step-by-step**.

---

## 🎯 Focus Topics

* What a **set** is used for (conceptually, not syntactically)
* How Python **creates and evaluates a set**
* How Python handles:

  * **Uniqueness**
  * **Membership checks**
  * **Add vs update vs recreate**

* Execution order in set operations

---

## 🧪 What I Plan to Do (Execution-First)

1. Read the **concept note on sets** (mental model first).
2. Write **execution predictions** before running each cell:

   * What values survive?
   * What gets removed?
3. Trigger **common set “surprises”**, such as:

   * Duplicate values silently disappearing
   * Using an unhashable item (e.g. list) inside a set
4. Reorder or refactor code to:

   * Fix errors
   * Change outcomes intentionally
5. Explain **each outcome in plain English**, focusing on:

   * What Python evaluated
   * When it evaluated it
   * Why the result looks the way it does

---

## Planned Experiments

Here’s a **drop-in, ready-to-run experiment pack** for **Data Structures — SETS**, written in the same **execution-first, predict-before-run** style. Paste this into `sandbox.ipynb` as separate cells.

---

# 🧠 EXPERIMENT PACK — DATA STRUCTURES: SETS (Execution View)

## ✅ Session Rule

**NO running** until you write a prediction above each cell:

* Does the set exist *yet*?
* What elements exist *right now*?
* Will Python succeed or throw an error?
* If it errors: *where* and *why*?

---

## 0) Setup: Print Helper

```python
def show(label, s):
    print(f"{label}: {s} | type={type(s).__name__} | size={len(s)}")
```

---

## 1) Set Creation Happens at Execution Time

```python
# PREDICT:
# - Does s exist before this line runs?
# - What will it contain after this line?

s = {1, 2, 3, 3, 2}
show("s after creation", s)
```

**What you should notice:** duplicates don’t survive — but **only after** Python executes the creation line.

---

## 2) Membership Test = Fast Question

```python
# PREDICT: True/False for each "in" check

s = {10, 20, 30}
print(20 in s)
print(99 in s)
```

**Mental model:** `in` asks the set: “Do you have this element RIGHT NOW?”

---

## 3) Trigger a Failure Intentionally (NameError + TypeError)

### 3A) NameError: Use the set before it exists

```python
# PREDICT: Which line fails? Why?

print("Is 1 in s?", 1 in s)
s = {1, 2, 3}
```

### 3B) TypeError: Unhashable element (list inside a set)

```python
# PREDICT: Does Python allow a list inside a set?

bad = {[1, 2], 3}
print(bad)
```

✅ **Expected:** TypeError about “unhashable type: 'list'”.

---

## 4) Mutation vs Replacement (The Big Set Rule)

```python
# PREDICT:
# - Will the name 's' change?
# - Will the *same set object* be updated?

s = {1, 2, 3}
show("start", s)

s.add(4)
show("after add(4)", s)

s.remove(2)
show("after remove(2)", s)

s = s.union({99})
show("after union({99})", s)
```

**Key idea:**

* `.add()` / `.remove()` → **mutate same set**
* `s = s.union(...)` → **creates new set, then rebinds name**

---

## 5) Remove vs Discard (Error vs No Error)

```python
# PREDICT:
# - Which one errors if element not present?

s = {1, 2, 3}
s.discard(999)
print("after discard(999):", s)

s.remove(999)   # should raise KeyError
print("you won't reach here")
```

**Traceback drill:** read **last line** = real error.

---

## 6) Ordering Trap: Sets Don’t Promise Order

```python
# PREDICT:
# - Will the printed order match your typing order?

s = {"banana", "apple", "orange", "mango"}
print(s)
```

**Rule:** sets are about **membership**, not order.

---

## 7) Set Ops: Union / Intersection / Difference (Value-Producing)

```python
# PREDICT outputs of each operation

a = {1, 2, 3, 4}
b = {3, 4, 5}

print("union:", a | b)
print("intersection:", a & b)
print("difference a-b:", a - b)
print("difference b-a:", b - a)
```

**Execution view:** these create **new sets** (they don’t mutate `a` or `b`).

---

## 8) Sequence Matters: Same Pieces, Different Order, Different Outcome

### 8A) Fails

```python
# PREDICT: Which line fails and why?

s = {1, 2, 3}
s.remove(4)
print("done")
```

### 8B) Works (reorder to avoid failure)

```python
# PREDICT: Why does this version not fail?

s = {1, 2, 3}
if 4 in s:
    s.remove(4)
print("done")
```

**Big insight:** most bugs are **timing/state bugs**: “does the element exist *right now*?”

---

## 9) Mini Boss Drill: Predict Final State

```python
# PREDICT final value of s

s = set()
s.add("a")
s.add("b")
s.add("a")
s.update(["c", "d", "d"])
s.discard("b")
print("final:", s)
```

---

# ✅ Your “Rules I Learned” (copy into rules_i_learned.md)

Write 3–5 rules like these (in your words):

1. **A set exists only after its creation line runs.**
2. **A set stores unique items — duplicates disappear at creation/add time.**
3. **`in` checks what exists RIGHT NOW (membership).**
4. **Some operations mutate (`add`, `remove`), others create a new set (`union`, `|`, `&`, `-`).**
5. **`remove` can crash (KeyError); `discard` won’t.**
6. **A set can only contain hashable (immutable-like) items (no lists/dicts).**

---

If you want, next I can generate:

* a **broken_examples.py** section for sets (10 intentional failures),
* a **5-year-old explanation** of “hashable” using toys/labels,
* or a **micro-quiz** where you predict tracebacks before running.


---
## ✅ Success Criteria (Mastery Checks)

By the end of the session:

* I can explain **why sets automatically remove duplicates**
* I can predict **what a set will contain before running the code**
* I can explain **when Python raises a TypeError with sets**
* I can explain the difference between:

  * **Modifying a set**
  * **Recreating a new set**
* I recorded at least **one reusable execution rule** about sets

---

## 🧠 Reusable Execution Rules to Look For (Hint)

You’re aiming to discover rules like:

> “Python builds the entire set first, then applies uniqueness.”

> “Set membership checks don’t care about order — only existence.”

> “Mutability decides whether Python updates an object or replaces it.”

(You’ll formalize the *exact wording* at the end of the session.)

---

## 🔁 Same Learning Loop, New Concept

Nothing else in your system changes:

* Same **prediction discipline**
* Same **micro-tests**
* Same **explain-out-loud requirement**
* Same **promotion to rules_i_learned.md**

Only the **concept lens** changes — from *execution order* → *execution + uniqueness*.

---

If you want, next we can:

* Build a **gold-standard concept note for Sets**
* Design **3 execution traps** that fool beginners
* Or convert this into a **Day-X notebook header** you can reuse verbatim

Your move 🚀
