
Perfect — this is a **clean, execution-first adaptation** of your session, keeping the **same learning loop** and simply swapping the concept.

Below is the **drop-in replacement** for **Data Structures — Lists**, written in the same mental-model style you’re using across your Python-learning-os.

---

## 🧠 SESSION GOALS FOR TODAY — **DATA STRUCTURES: LISTS**

**Big idea:**
Python treats a **list** as a **container object** that already exists in memory, and your code interacts with it **step-by-step, top → bottom**.

Python does **not** “look ahead” inside lists.
Each list operation happens **only when execution reaches that line**.

---

## 🎯 Focus Topics

1. What a **list is in memory** (a container holding references)
2. How Python **creates a list** at execution time
3. How Python **accesses list elements by index**
4. Why **IndexError** happens (and when it does *not*)
5. How **mutation** changes a list *without* changing its name

---

## 🛠️ What I Plan to Do

### 1️⃣ Read Concept Note — *Python Lists (Execution View)*

Focus on:

* When a list is **created**
* When its **elements become accessible**
* The difference between:

  * ❌ “The list exists”
  * ✅ “This index exists *right now*”

---

### 2️⃣ Write Execution Predictions (Before Running)

Before running each cell, I will **predict**:

* Does the list exist at this line?
* Does this index exist at this moment?
* Will Python succeed or stop with an error?

> **Rule:** No running code until I explain *what Python will do next*.

---

### 3️⃣ Trigger a Failure Intentionally (IndexError)

I will:

* Access a list index **before it exists**
* Observe where Python stops
* Read the traceback **line number + message**
* Explain the failure in plain English

> *“Python reached this line, tried to grab an item that wasn’t there yet, and stopped.”*

---

### 4️⃣ Reorder Code to Make It Work

I will:

* Move list creation or list growth **above** the failing line
* Re-run the code
* Observe that **nothing else changed — only order**

> Same code pieces.
> Different execution order.
> Different outcome.

---

### 5️⃣ Explain Each Outcome in Plain English

For every result, I will explain:

* What Python **knew at that moment**
* What Python **did not know yet**
* Why the operation was allowed or rejected

No jargon.
No “because Python says so.”
Only execution logic.

---

## Planned Experiments

# ============================================================
# 🧪 EXPERIMENT PACK — DATA STRUCTURES: LISTS (Execution View)
# Paste into sandbox.ipynb (one cell at a time).
#
# RULE: Before running each cell, write your prediction:
# - Does the list exist YET?
# - Does this index exist RIGHT NOW?
# - Will Python succeed or stop (IndexError)?
# ============================================================


# ============================================================
# CELL 0 — Session Header (keep this at top)
# ============================================================
print("SESSION: Lists (Execution View)")
print("Goal: predict list existence + index existence BEFORE running")
print("-" * 50)


# ============================================================
# CELL 1 — List is created ONLY when this line runs
# ============================================================
# PREDICT:
# 1) Does nums exist before line 1 executes? (no)
# 2) After line 1, what is nums? (a list in memory)
nums = [10, 20, 30]
print("nums is:", nums)
print("len(nums) is:", len(nums))


# ============================================================
# CELL 2 — Index access succeeds only if that index exists NOW
# ============================================================
# PREDICT:
# nums[0] -> ?
# nums[2] -> ?
# nums[3] -> succeed or IndexError?
nums = [10, 20, 30]
print("nums[0] =", nums[0])
print("nums[2] =", nums[2])
print("nums[3] =", nums[3])  # 💥 IndexError (predict it)


# ============================================================
# CELL 3 — “Timing bug”: same ingredients, wrong order
# ============================================================
# PREDICT:
# Does nums exist when Python reaches print(nums)?
print(nums)         # 💥 NameError (predict it)
nums = [1, 2, 3]


# ============================================================
# CELL 4 — Fix by reordering (nothing else changes)
# ============================================================
# PREDICT:
# Will it print successfully now?
nums = [1, 2, 3]
print(nums)


# ============================================================
# CELL 5 — Index exists only after the element is added
# ============================================================
# PREDICT:
# At the moment of nums[0], does index 0 exist?
nums = []
print("nums is:", nums)
print("Trying nums[0]...")
print(nums[0])      # 💥 IndexError (predict it)


# ============================================================
# CELL 6 — Fix by growing the list BEFORE indexing
# ============================================================
# PREDICT:
# After append, does index 0 exist?
nums = []
nums.append("first")
print("nums is:", nums)
print("nums[0] =", nums[0])


# ============================================================
# CELL 7 — Mutation changes the SAME list object (name stays)
# ============================================================
# PREDICT:
# Does nums change “in place” after append?
nums = ["a", "b"]
print("before:", nums, "| id:", id(nums))
nums.append("c")
print("after: ", nums, "| id:", id(nums))  # same id => same object


# ============================================================
# CELL 8 — Rebinding changes what the NAME points to
# ============================================================
# PREDICT:
# Does id(nums) change after nums = nums + [...] ?
nums = ["a", "b"]
print("before:", nums, "| id:", id(nums))
nums = nums + ["c"]  # creates NEW list, then rebinds name
print("after: ", nums, "| id:", id(nums))  # different id => new object


# ============================================================
# CELL 9 — Two names, one list (aliasing trap)
# ============================================================
# PREDICT:
# If you change a, does b also “change”? Why?
a = [1, 2]
b = a
print("a:", a, "| id:", id(a))
print("b:", b, "| id:", id(b))
a.append(3)
print("after a.append(3)")
print("a:", a)
print("b:", b)  # b changed too (same underlying list)


# ============================================================
# CELL 10 — IndexError vs “safe check”
# ============================================================
# PREDICT:
# Which line is safe and why?
nums = [9]
print("len(nums):", len(nums))

# unsafe:
# print(nums[1])  # 💥 IndexError (uncomment to prove)

# safe:
if len(nums) > 1:
    print("nums[1] =", nums[1])
else:
    print("Index 1 does not exist right now")


# ============================================================
# CELL 11 — Negative indexing (still must exist!)
# ============================================================
# PREDICT:
# nums[-1] -> ?
# nums[-3] -> ?
nums = [10, 20]
print("nums[-1] =", nums[-1])
print("nums[-3] =", nums[-3])  # 💥 IndexError (predict it)


# ============================================================
# CELL 12 — Slice is “forgiving” (does NOT raise IndexError)
# ============================================================
# PREDICT:
# Does slicing crash if range is too big?
nums = [10, 20, 30]
print("nums[0:10] =", nums[0:10])     # returns what exists
print("nums[10:20] =", nums[10:20])   # returns [] (empty), no crash


# ============================================================
# CELL 13 — Pop: mutation + possible IndexError
# ============================================================
# PREDICT:
# What does pop return? What happens when list is empty?
nums = ["x", "y"]
item = nums.pop()
print("popped:", item)
print("nums now:", nums)

nums = []
print("trying pop on empty...")
print(nums.pop())  # 💥 IndexError (predict it)


# ============================================================
# CELL 14 — Your “Execution Rules” (write as prints)
# ============================================================
# Fill in your own rules after the session.
rules = [
    "A list exists only after its line executes.",
    "An index exists only after the element is added.",
    "Python cares about what exists RIGHT NOW, not what I intend.",
    "Most list bugs are TIMING bugs (order), not syntax bugs."
]
print("\nRULES I LEARNED:")
for r in rules:
    print("-", r)


# ============================================================
# CELL 15 — Challenge Drill (predict WITHOUT running first)
# ============================================================
# Write your prediction in a comment, then run.
nums = []
nums.append(10)
nums.append(20)
print("A:", nums[1])

nums = nums + [30]
print("B:", nums)

nums.pop()
print("C:", nums)

print("D:", nums[2])  # will this succeed or IndexError? predict!

---

## ✅ Success Criteria (Checklist)

By the end of this session:

* ✅ I can explain **how Python walks through a list line by line**
* ✅ I can predict **IndexError before running code**
* ✅ I can explain why **reordering list operations fixes errors**
* ✅ I recorded **at least one reusable execution rule** about lists

---

## 🧩 Example Reusable Execution Rules (What You’re Aiming to Write)

You should end with rules like:

* **“A list exists only after its line executes.”**
* **“An index exists only after the element is added.”**
* **“Python does not care what I *intend* — only what exists *right now*.”**
* **“Most list bugs are timing bugs, not syntax bugs.”**

---

## 🔁 How This Fits Your Learning OS

* 📄 **Concept note** → `notes/core/lists_execution_model.md`
* 🧪 **Predictions + tests** → `sandbox.ipynb`
* 💥 **Intentional failures** → `broken_examples.py`
* 🧠 **Distilled rule** → `rules_i_learned.md`

Same workflow.
New concept.
Deeper intuition.

---

If you want, next we can:

* Build a **5-year-old explanation** of lists
* Create **IndexError vs NameError contrast drills**
* Or promote this into a **gold-standard “Lists” concept template**

Just say the word 👌
