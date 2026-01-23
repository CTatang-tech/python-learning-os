
Below is a **one-page, execution-first conceptual summary** synthesised from your attached notes on **lists, tuples, dicts, sets, and mutability** .

---

# 🧠 Python Execution, Errors, and Failure Reasoning

*(One-Page Conceptual Summary)*

---

## 1️⃣ How Python Executes Code (Core Mental Model)

* Python runs **top → bottom, one line at a time**
* Python **does not look ahead**
* At each line, Python asks:

  * Does this **name exist right now**?
  * Does this **object allow this operation**?
  * Does this **index / key / element exist right now**?

If the answer is **no**, execution **stops immediately**.

> Python executes reality, not intention.

---

## 2️⃣ Objects, Names, and Time

* Names are **bound to objects at execution time**
* Objects:

  * **exist only after** their creation line runs
  * have rules (mutable vs immutable)
* “Future lines” do not count as knowledge

Key idea:

* **Existence is temporal**
* Python reasons in **“now”**, not “later”

---

## 3️⃣ Containers: What Python Enforces Internally

### Lists

* Mutable, ordered containers
* Index exists **only after element is added**
* Most failures are **timing errors**, not syntax errors

Python’s rule:

> “You asked for position *n*. I checked. It’s not there.”

---

### Tuples

* Immutable, ordered containers
* Python **protects the structure**
* Any attempt to change an element → immediate failure

Important distinction:

* Container is immutable
* Contents *inside* may still be mutable

Python’s rule:

> “I allow reading. I refuse editing.”

---

### Dictionaries

* Mutable mapping: **keys → values**
* Keys must exist **at lookup time**
* Missing key ≠ missing variable

Python distinguishes:

* **NameError** → container doesn’t exist
* **KeyError** → container exists, key doesn’t

Python’s rule:

> “I won’t guess a key that isn’t there.”

---

### Sets

* Mutable collections of **unique elements**
* Order is irrelevant
* Membership is the core operation

Python enforces:

* Uniqueness automatically
* Elements must be **hashable**

Python’s rule:

> “I care about existence, not position.”

---

## 4️⃣ Mutability: The Hidden Execution Switch

Mutability answers one question:

> Does Python **update the object**, or **replace it**?

* Mutable → object updated **in place**
* Immutable → new object created, name rebound

Consequences:

* Multiple names may see the same change
* Bugs appear when structure choice is wrong

---

## 5️⃣ How Errors Arise (Execution View)

Errors happen when Python hits a line that violates reality:

* **NameError**
  → “This name does not exist *yet*”

* **IndexError**
  → “This position does not exist *now*”

* **KeyError**
  → “This key does not exist *now*”

* **TypeError**
  → “This operation is forbidden for this object”

Python does **not recover**, **skip**, or **continue** past errors.

---

## 6️⃣ How to Reason About Failures (Step-by-Step)

When something fails, ask in this order:

1. **Where did execution stop?**
2. **What object was Python touching?**
3. **What rule did that object enforce?**
4. **Did the object exist at that moment?**
5. **Was Python asked to read or to modify?**

Most bugs resolve by:

* Reordering lines
* Choosing the correct structure
* Replacing unsafe access with safe access

---

## 7️⃣ Common Beginner Mistakes (Pattern-Level)

* Assuming objects or keys exist before creation
* Using immutable structures where updates are required
* Treating execution errors as syntax problems
* Forgetting that assignment copies **references**, not objects
* Expecting Python to “figure it out”

---

## 8️⃣ Rules of Thumb to Remember

* **Python only knows what has already executed**
* **Mutability decides: update vs replace**
* **Most bugs are timing bugs, not logic bugs**
* **Containers enforce their own rules**
* **If execution surprises you, check object type + moment**

---

## 🏁 Final Mental Anchor

> **Python executes the present, enforces object rules strictly, and stops the moment reality is violated.**

If you want next, this can be:

* distilled into a **laminated cheat-sheet**, or
* converted into a **debugging decision tree**, or
* promoted into your **core “Execution Model” note** for long-term reuse.
