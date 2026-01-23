


# 🧠 SESSION GOALS FOR TODAY — **DATA STRUCTURES: DICTIONARIES (key-value pairs)**

**Big idea:**
A dictionary is a **mapping object** that Python executes **line-by-line**, just like any other object — but **key access has rules** that can break execution if misunderstood.

Python still:
👉 runs **top → bottom**
👉 raises errors **the moment a rule is violated**

---

## 🎯 Focus Topics

* What a **dictionary is at execution time**
* How Python **creates** a dict in memory
* What happens when Python **looks up a key**
* Difference between:

  * **NameError** (dict not defined)
  * **KeyError** (key not found)
* How **reordering lines** or **changing access methods** fixes errors

---

## 🛠️ What I Plan to Do

### 1️⃣ Read Concept Note — *Dictionaries (Execution View)*

Focus on:

* When a dictionary **comes into existence**
* How Python executes:

  ```python
  data = {"a": 1, "b": 2}
  ```
* Why `data["c"]` can crash execution
* Why `data.get("c")` does **not**

---

### 2️⃣ Write Execution Predictions (Before Running)

Before running each cell, I will write:

* ✅ “This line will run”
* ❌ “This line will crash”
* ❓ “This will return a value or raise an error?”

Example prediction questions:

* What happens if I access a key **before the dict exists**?
* What happens if the dict exists but the **key doesn’t**?
* Does Python “look ahead” to see future keys? (Spoiler: **NO**)

---

### 3️⃣ Trigger Execution Errors on Purpose

#### 🔴 Error Type 1 — **NameError**

Accessing a dictionary **before it is defined**

```python
print(user["name"])
user = {"name": "Collins"}
```

➡️ Predict the error
➡️ Run
➡️ Explain why Python fails **at that exact line**

---

#### 🔴 Error Type 2 — **KeyError**

Dictionary exists, but key does not

```python
user = {"name": "Collins"}
print(user["age"])
```

➡️ Predict
➡️ Run
➡️ Explain why Python crashes **even though the dict exists**

---

### 4️⃣ Reorder or Refactor Code to Make It Work

#### Fix 1️⃣ — Reorder execution

```python
user = {"name": "Collins"}
print(user["name"])
```

#### Fix 2️⃣ — Safer access

```python
user = {"name": "Collins"}
print(user.get("age"))
```

➡️ Explain:

* Why this no longer crashes
* What Python returns instead
* Why execution continues

---

### 5️⃣ Explain Each Outcome in Plain English

I will explain each result as if to a **5-year-old**, focusing on:

* When Python **knows something**
* When Python **doesn’t**
* Why Python **refuses to guess**

Example explanation style:

> “Python opens the dictionary.
> It looks for the key.
> If the key is missing, Python stops and shouts.”

---

### Planned Experiments

## 🧠 SESSION GOALS FOR TODAY — **DATA STRUCTURES: DICTIONARIES**

**Big idea:**
Python treats a **dictionary (`dict`)** as a **container object in memory** that maps **keys → values**.
Your code interacts with it **step-by-step, top → bottom**.

Python does **not** “look ahead.”
A key only “exists” **after the line that creates it has executed**.

---

## 🎯 Focus Topics

1. What a **dict is in memory** (a container mapping keys to values)
2. When a dict is **created** during execution
3. How Python **looks up values by key**
4. Why **KeyError** happens (and when it does *not*)
5. How **mutation** changes a dict *without* changing its name

---

# ✅ Ready-to-run Experiment Pack (paste into `sandbox.ipynb`)

> **Rule:** Before you run each cell, write your prediction in a comment:
> ✅ “What will print?” ✅ “Will it crash?” ✅ “What will the dict look like after?”

---

## 1️⃣ Dict Creation Happens at That Line

```python
# PREDICT: Will this work? Why/why not?

print("Before creation…")
# print(profile)  # Uncomment to intentionally trigger NameError

profile = {"name": "Ada", "age": 12}
print("After creation:", profile)
print("Keys now:", list(profile.keys()))
```

**Prediction prompts**

* Does `profile` exist before its assignment line?
* When do keys become “real”?

---

## 2️⃣ Key Lookup is “NOW”, Not “Intended” (Trigger KeyError)

```python
# PREDICT: Which line fails? What was Python trying to do?

student = {"name": "Collins", "level": "beginner"}
print("student:", student)

print(student["name"])     # should work
print(student["score"])    # KeyError (score doesn't exist yet)

student["score"] = 95
print("Now score exists:", student["score"])
```

**Your explanation (plain English):**
“Python reached this line, tried to fetch a key that wasn’t there, and stopped.”

---

## 3️⃣ Make It Safe: `get()` vs `[]`

```python
# PREDICT: What prints? Does anything crash?

user = {"username": "neo"}

print(user.get("username"))        # exists
print(user.get("email"))           # missing → returns None
print(user.get("email", "N/A"))    # missing → default value
# print(user["email"])             # Uncomment to trigger KeyError
```

**Rule you’re aiming to learn:**

* `dict["k"]` = “MUST exist.”
* `dict.get("k")` = “If it exists, give it. If not, give None/default.”

---

## 4️⃣ Reorder Code to Fix the Error (Timing Bug)

### Version A (broken on purpose)

```python
# PREDICT: Where does it fail?

settings = {}
print(settings["theme"])     # KeyError
settings["theme"] = "dark"
print("Theme:", settings["theme"])
```

### Version B (same pieces, different order)

```python
# PREDICT: Now what happens?

settings = {}
settings["theme"] = "dark"
print("Theme:", settings["theme"])
```

**Key learning:**
Same code pieces. Different order. Different outcome.

---

## 5️⃣ Mutation vs Replacement (Watch the “same dict” change)

```python
# PREDICT:
# - Will the id change after mutation?
# - Will it change after replacement?

d = {"count": 1}
print("start:", d, "id:", id(d))

# MUTATION (update the existing dict)
d["count"] = d["count"] + 1
print("after mutation:", d, "id:", id(d))

# REPLACEMENT (rebind name to a new dict)
d = {"count": 999}
print("after replacement:", d, "id:", id(d))
```

**Mental model:**

* Mutation = “same container, new contents.”
* Replacement = “new container, same name.”

---

## 6️⃣ Keys Must Be Hashable (Trigger TypeError)

```python
# PREDICT: Will this work? What error? Why?

bad = {}
bad[[1, 2, 3]] = "oops"   # lists are unhashable → TypeError
```

Then try a valid key:

```python
good = {}
good[(1, 2, 3)] = "ok"    # tuple is hashable
print(good)
```

---

## 7️⃣ Nested Dict Access (KeyError vs safe chained access)

```python
# PREDICT: What prints? Where can it fail?

data = {
    "user": {
        "profile": {"name": "Sam"}
    }
}

print(data["user"]["profile"]["name"])  # should work

# Make it fail on purpose:
# print(data["user"]["profile"]["age"])  # KeyError

# Make it safe:
print(data["user"]["profile"].get("age", "unknown"))
```

---

## 8️⃣ Looping: Keys, Values, Items (and “order” isn’t your logic)

```python
# PREDICT: What prints? How many lines?

scores = {"A": 10, "B": 20, "C": 30}

for k in scores:
    print("key:", k)

for v in scores.values():
    print("value:", v)

for k, v in scores.items():
    print(k, "→", v)
```

---

## 9️⃣ Debug Drill: Fix One Error per Run

### Bug: KeyError

```python
cart = {"apples": 2}
total = cart["apples"] + cart["bananas"]   # KeyError
print(total)
```

✅ Fix options (pick one):

* Add the key before using it
* Use `.get("bananas", 0)`
* Use `setdefault`

Try:

```python
cart = {"apples": 2}
total = cart["apples"] + cart.get("bananas", 0)
print(total)
```

**Record in your daily-log**

1. Original error: ___
2. Where it failed: ___
3. Fix applied: ___
4. Lesson learned: ___

---

# ✅ Success Criteria Checklist (Paste into your notebook)

* [ ] I can explain: **a dict exists only after its creation line runs**
* [ ] I can predict **KeyError before running**
* [ ] I can explain why **reordering dict lines fixes errors**
* [ ] I can explain **get() vs []**
* [ ] I wrote 1 reusable rule about dictionaries

---

# 🧩 Reusable “Rules I Learned” (aim to write one of these)

* **“A key exists only after the line that creates it executes.”**
* **“KeyError means: I asked for a key that doesn’t exist right now.”**
* **“Use `[]` when the key MUST exist; use `get()` when missing is OK.”**
* **“Most dict bugs are timing bugs (when the key is created) not syntax bugs.”**
* **“Mutation updates the same dict; replacement makes a new dict.”**

If you want, I can also generate a matching **broken_examples.py** section (pure failure drills) for dictionaries, aligned 1:1 with these experiments.


---

## ✅ Success Criteria (Execution-Aware)

By the end of the session:

* ✅ I can explain **how Python builds a dictionary line-by-line**
* ✅ I can predict **NameError vs KeyError before running**
* ✅ I can explain **why reordering lines fixes execution**
* ✅ I can explain why `.get()` prevents crashes
* ✅ I recorded **at least one reusable execution rule**

---

## 🧩 Reusable Execution Rules I Expect to Record

You should aim to capture rules like:

* **Python must see a dictionary before you can use it**
* **Keys must exist at lookup time or execution stops**
* **`.get()` changes failure into a safe return**
* **Execution errors happen immediately — Python never skips a bad line**

---

## 🔑 One-Line Mental Model (Keep This)

> **A dictionary is a box Python opens line-by-line.
> If the box or the key isn’t there, execution stops immediately.**

---

If you want, next we can:
👉 turn this into a **broken_examples.py drill**, or
👉 promote the final rules into `rules_i_learned.md`, or
👉 adapt the same structure for **sets** or **lists**.

Your call 🚀
