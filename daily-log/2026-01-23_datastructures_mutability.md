

## 🧠 SESSION GOALS — DATA STRUCTURES: MUTABILITY & STRUCTURE CHOICE

### 🎯 Big Goal for Today

Understand **how Python treats different data structures in memory**, and how **mutability drives whether Python updates data in place or creates a new object** — which directly affects correctness, bugs, and performance.

This is not about syntax.
It’s about **what Python actually does under the hood**.

---

## 🔍 Focus Topics

* **Mutability vs immutability**
* **Structure choice**: list vs tuple vs dict vs set
* **Update vs replace** (in-place change vs rebinding)
* How mutability affects:

  * Variable references
  * Function behavior
  * Bugs that “feel like magic”

---

## 🧪 What I Plan to Do (In Order)

1. **Read concept note** on mutability & structure choice

   * Focus on *mental models*, not examples.

2. **Predict behavior before running code**

   * Ask before every cell:

     * *Will this update the object, or replace it?*
     * *Will other references see the change?*

3. **Trigger a mutation surprise**

   * Modify a list or dict and observe:

     * Another variable changing “unexpectedly”

4. **Trigger a rebinding contrast**

   * Reassign an immutable structure (tuple / string / int)
   * Observe that the original object is untouched

5. **Fix behavior by choosing the right structure**

   * Replace:

     * list → tuple (when safety is needed)
     * tuple → list (when updates are needed)
     * list → dict (when lookup matters)

6. **Explain each outcome in plain English**

   * No jargon
   * “Python did X because this structure is mutable/immutable”

---

## Planned Experiments

Below is a **ready-to-run experiment pack** you can paste straight into `sandbox.ipynb` for:

# ✅ Data Structures — **Mutability & Structure Choice** (Execution View)

**Rule for today:** No running until you **predict what changes** and **what stays the same**.

---

## 🧪 CELL 0 — Session Header (Markdown in notebook)

Paste this as a Markdown cell:

* **Concept:** Mutability & Structure Choice
* **Big idea:** Some objects can be **changed in place** (mutated). Others can’t — they must be **replaced**.
* **Success = I can predict:**

  1. when an object changes *without* changing its name
  2. when a name gets rebound to a brand new object
  3. which structure to pick (list/dict/set/tuple) based on the job

---

## 🧪 CELL 1 — Setup Helpers (run this)

```python
def show(label, obj):
    print(f"{label}: value={obj!r} | type={type(obj).__name__} | id={id(obj)}")

print("Ready.")
```

---

## Experiment 1 — **Mutate vs Replace** (List vs Tuple)

### 🧠 Predict BEFORE running:

* Will the **id** change?
* Will the **value** change?
* Will it error?

```python
# LIST: mutable
a = [1, 2, 3]
show("a (start)", a)

a.append(4)
show("a (after append)", a)

a = a + [5]           # watch what happens here
show("a (after +)", a)

print("-" * 40)

# TUPLE: immutable
t = (1, 2, 3)
show("t (start)", t)

# Predict: error or not?
try:
    t.append(4)
except Exception as e:
    print("t.append error:", type(e).__name__, "-", e)

# Predict: id change or not?
t = t + (4,)
show("t (after +)", t)
```

✅ **What you’re learning:**

* **Mutate** = same object id, new contents
* **Replace** = new object id, new contents, same variable name

---

## Experiment 2 — **Two Names, One Object** (Alias Trap)

### 🧠 Predict:

* When you change `a`, does `b` change too?

```python
a = [10, 20]
b = a

show("a", a)
show("b", b)

a.append(30)

print("After a.append(30):")
show("a", a)
show("b", b)

print("a is b:", a is b)
```

✅ Rule you should write after:
**“Assignment does not copy the object — it copies the reference.”**

---

## Experiment 3 — **Copy vs Shared Reference** (Fix the Trap)

### 🧠 Predict:

* Which one changes together, which one stays independent?

```python
a = [1, 2]
b = a          # shared
c = a.copy()   # separate

a.append(99)

print("After a.append(99):")
print("a:", a)
print("b:", b)
print("c:", c)

print("a is b:", a is b)
print("a is c:", a is c)
```

---

## Experiment 4 — **Dict Mutability + Missing Keys** (Structure choice trigger)

### 🧠 Predict:

* Which lines mutate the dict?
* Which lines can crash?

```python
user = {"name": "Collins", "role": "admin"}
show("user (start)", user)

user["role"] = "viewer"          # mutation
show("user (after role change)", user)

# Predict: crash or safe?
try:
    print("age:", user["age"])
except Exception as e:
    print("user['age'] error:", type(e).__name__, "-", e)

# Safe pattern
print("age (safe get):", user.get("age", "UNKNOWN"))

user["age"] = 42                 # mutation
show("user (after add age)", user)
```

✅ Structure choice takeaway:
Use a **dict** when you need **named fields** and **fast lookups** by key.

---

## Experiment 5 — **Set: uniqueness + mutability**

### 🧠 Predict:

* What happens to duplicates?
* Does set keep order?

```python
s = set()
show("s (start)", s)

s.add("apple")
s.add("apple")
s.add("banana")

show("s (after adds)", s)
print("Contains apple?", "apple" in s)
```

✅ Structure choice takeaway:
Use a **set** when you care about **uniqueness** and **membership checks**.

---

## Experiment 6 — **Strings: “Looks mutable” but aren’t**

### 🧠 Predict:

* Will `id` change after `.upper()`?
* Does `upper()` mutate or replace?

```python
name = "collins"
show("name (start)", name)

up = name.upper()
show("name (after upper call)", name)
show("up", up)
```

✅ Rule:
**String methods create NEW strings. They don’t mutate the original.**

---

## Experiment 7 — **Compound assignment `+=` (Mutability decides the behavior)**

### 🧠 Predict:

* Does `+=` mutate or replace for list? for tuple? for str?

```python
# LIST
a = [1, 2]
show("a (start)", a)
a += [3]       # often mutates in place
show("a (after +=)", a)

print("-" * 40)

# TUPLE
t = (1, 2)
show("t (start)", t)
t += (3,)      # must replace
show("t (after +=)", t)

print("-" * 40)

# STRING
s = "hi"
show("s (start)", s)
s += "!"
show("s (after +=)", s)
```

✅ Your reusable punchline:
**“Mutability decides: update vs replace.”**

---

## Experiment 8 — **Structure Choice Mini-Drills** (Pick the right tool)

Paste + answer in comments:

```python
# For each scenario, pick: list / tuple / dict / set
# Then say WHY in one short line.

# 1) Track steps in a workflow, order matters, you’ll add/remove steps.
# answer =

# 2) Store settings that should never change once created (like a fixed config key).
# answer =

# 3) Store a user profile with named fields: name, age, role, country.
# answer =

# 4) Track unique visitor IDs (no duplicates) and quickly check if someone visited.
# answer =
```

---

## Experiment 9 — **One Bug + Traceback** (Mutability misunderstanding)

### 🧠 Predict the error first:

```python
nums = (1, 2, 3)
nums[0] = 99
```

Then fix it **two ways** (after you see the error):

1. Choose a mutable structure
2. Replace the entire tuple (create a new one)

---

# ✅ “Rules I Learned” (copy to `rules_i_learned.md`)

Write these after the run (edit in your own words):

1. **Mutable objects** can change *without changing their id* (list, dict, set).
2. **Immutable objects** can’t change — you must **replace** them (tuple, str, int).
3. `b = a` does **not copy** the object — it copies the **reference**.
4. If two names point to the same mutable object, a change through one name shows up in the other.
5. **Structure choice is a job choice:**

   * **list** = ordered, changeable sequence
   * **tuple** = ordered, fixed sequence
   * **dict** = named fields / key lookup
   * **set** = unique items / membership checks

---

If you want, next I can generate a matching `broken_examples.py` section for **mutability traps** (aliasing, accidental shared lists, dict default pitfalls) so you can drill them the same way you do NameError/IndexError.

---

## ✅ Success Criteria (Non-Negotiable)

By the end of the session:

1. **I can explain mutability without using the word “mutable”**

   * Example: “This thing can be changed without creating a new one.”

2. **I can predict update vs replace before execution**

   * I know *in advance* whether Python will:

     * modify the existing object, or
     * bind the name to a new object

3. **I can justify structure choice**

   * I can clearly say:

     * “This should be a list because…”
     * “This must be a tuple because…”
     * “This should be a dict because lookup matters”

4. **I recorded at least ONE reusable rule**

   * Added to `rules_i_learned.md`
   * Example pattern:

     > “If multiple names point to the same mutable object, changes are shared.”

---

## 🧠 Mental Anchor (Carry This All Day)

> **Mutability decides: UPDATE vs REPLACE**
>
> Python doesn’t “change variables”.
> It either:
>
> * updates an object **in place**, or
> * rebinds a name to a **new object**

Everything else is noise.

---

## 🔁 Promotion Rule (Same OS Discipline)

* **Notebook** → raw observations
* **Daily log** → what surprised me
* **Notes/** → stable explanation of mutability
* **Rules I learned** → short, testable truths

No skipping steps.

---

If you want, next we can:

* Convert this into a **concept note file** (`notes/core/mutability.md`)
* Design **mutation traps** (classic interview / bug patterns)
* Build a **structure choice decision table** (production-grade)

Just say the word.
