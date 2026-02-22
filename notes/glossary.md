# Term: Updating
- Plain definition: Updating means replacing a variable's old value with a new value.
- Why it matters: You need to know that when you update, the old value is **gone forever**—it doesn't exist alongside the new value.

- Example: `X = 5; X = 10` → X is now 10, not "both 5 and 10"

- Common confusion: **UPDATING vs. REASSIGNMENT**

**Reassignment**: Technical term for the mechanism (using `=` to bind a new value to a name)
**Updating**: Emphasizes that we're *changing* an existing variable that already has a value
- *Why confusing*: Both use `=` and both change the variable
- *Key difference*: Reassignment is the HOW (the syntax/mechanism), updating is the WHY/CONTEXT (we're modifying something that existed before)

# Term: Rebinding
- Plain definition: Rebinding means making a name point to a different value (redirecting the label to something new).
- Why it matters: Helps you understand that variables are *names for values*, not containers. You're changing which value the name points to, not modifying the value itself.

- Example: `X = 5; X = 10` → The name X now points to 10 instead of 5

- Common confusion: **REBINDING vs. REFERENCE**

**Reference**: Means "pointing to" or "using" a value; just *reading* what a name points to (no change)
**Rebinding**: Means *changing* what a name points to; actively breaking the old connection and creating a new one
- *Why confusing*: Both involve names pointing to values, so they seem similar
- *Key difference*: Reference is **static/read-only** (just accessing the current value), rebinding is **dynamic/changing** (breaking and remaking the connection)
- *Example*: `y = X + 2` creates a **reference** to X (reads its value). `X = 10` **rebinds** X (changes what it points to)

# Term: Traceback
- Plain definition: A traceback is a map showing the path Python took through your code before hitting an error.
- Why it matters: It tells you *where* the error happened and *how it got there*, making debugging possible instead of guessing.

- Example: Shows `Cell In[12], line 2` → `age + "years"` so you know exactly which line broke

- Common confusion: **TRACEBACK vs. ERROR MESSAGE**

**Error Message**: The **final verdict** — the type and description of what went wrong
**Traceback**: The **entire map/path** showing how Python got to the error
- *Why confusing*: People say "I got a traceback" when they mean "I got an error." But a traceback is the *entire output* including the error message at the bottom
- *Key difference*: Traceback answers "WHERE & HOW did it break?" Error message answers "WHAT broke & WHY?" You need **both** to debug well. Traceback = directions, Error message = diagnosis
- *Example*: Traceback = `Cell In[12], line 2` + `age + "years"` | Error message = `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

# Term: Concatenate
- Plain definition: Concatenate means joining two or more strings (or sequences) together end-to-end to create a single combined string.
- Why it matters: String concatenation is one of the most common operations in programming. Understanding it helps you combine text, build messages, and manipulate strings effectively.

- Example: `"Hello" + " " + "World"` → `"Hello World"` or `name = "Alice"; greeting = "Hi, " + name` → `"Hi, Alice"`

- Common confusion: **CONCATENATION vs. ADDITION**

- **Addition**: Combining numbers mathematically (5 + 3 = 8)
- **Concatenation**: Joining strings end-to-end (no math, just combining text)
- *Why confusing*: Both use the `+` operator, but they do different things depending on data type
- *Key difference*: Addition is **mathematical** (produces a numeric result), concatenation is **textual** (produces a string result). Addition requires numbers, concatenation works with strings
- *Example*: `5 + 3` equals `8` (addition), but `"5" + "3"` equals `"53"` (concatenation). Different operators conceptually, same symbol `+`

# Term: Casting
- Plain definition: Casting (or type conversion) is the process of changing a value from one data type to another using built-in functions like int(), str(), or float().
- Why it matters: Python doesn't automatically convert types for operations, so casting lets you make incompatible types compatible and avoid TypeErrors.

- Example: `int("42")` converts the string "42" to the integer 42, allowing math operations.

- Common confusion: **CASTING vs. AUTOMATIC CONVERSION**

- **Automatic Conversion**: Python sometimes converts types implicitly (e.g., int to float in addition), without your code asking for it.
- **Casting**: You explicitly call a function to convert the type yourself.
- *Why confusing*: Both change types, but casting is manual and required for strings/numbers mixing.
- *Key difference*: Automatic conversion happens behind the scenes (e.g., 5 + 3.0 = 8.0), casting requires your code (e.g., int("5") + 3).
- *Example*: `5 + 3.0` uses automatic conversion; `int("5") + 3` uses casting.

# Term: Type Compatibility
- Plain definition: Type compatibility means whether Python can perform operations between values of different types without raising a TypeError.
- Why it matters: It explains why some operations work (e.g., int + int) and others fail (e.g., int + str), helping you predict and fix errors.

- Example: `5 + 10` works (both int); `5 + "10"` fails (TypeError).

- Common confusion: **TYPE COMPATIBILITY vs. TYPE CONVERSION**

- **Type Conversion**: Changing a value's type (e.g., via casting).
- **Type Compatibility**: Whether types can interact in an operation without change.
- *Why confusing*: Both relate to types in operations, but compatibility is about "can they work together?" while conversion is about "how to make them work."
- *Key difference*: Compatibility checks if it's possible as-is; conversion fixes incompatibility.
- *Example*: int and str are incompatible for addition; convert str to int for compatibility.

# Term: TypeError
- Plain definition: A TypeError occurs when you try to perform an operation on incompatible types (e.g., adding a number and a string).
- Why it matters: It's Python's way of saying "these types don't mix," forcing you to fix type mismatches explicitly.

- Example: `5 + "hello"` raises TypeError: unsupported operand type(s) for +: 'int' and 'str'.

- Common confusion: **TYPEERROR vs. VALUEERROR**

- **TypeError**: Wrong types for the operation (e.g., int + str).
- **ValueError**: Right type, but invalid value (e.g., int("abc")).
- *Why confusing*: Both are errors, and messages mention "types" or "values."
- *Key difference*: TypeError is about type mismatch; ValueError is about content within the type.
- *Example*: `5 + "5"` → TypeError (types); `int("abc")` → ValueError (value).

# Term: Argument
- Plain definition: An argument is a value passed to a function when calling it, providing the data the function will operate on.
- Why it matters: Arguments make functions flexible and reusable by allowing them to work with different inputs each time they're called.

- Example: In `len("hello")`, the string "hello" is the argument passed to the len() function.

- Common confusion: **ARGUMENT vs. PARAMETER**

- **Parameter**: The variable name defined in the function's signature that receives the value.
- **Argument**: The actual value passed to the function when calling it.
- *Why confusing*: Both refer to function inputs, but they're used at different times in the code.
- *Key difference*: Parameters are placeholders in the function definition; arguments are the concrete values provided at call time.
- *Example*: `def greet(name):` (name is a parameter); `greet("Alice")` ("Alice" is an argument).

# Term: Variable
- Plain definition: A variable is a name that refers to a value stored in memory, allowing you to access and manipulate data using meaningful identifiers.
- Why it matters: Variables make code readable and reusable by giving names to values instead of using raw data everywhere.

- Example: `age = 25; print(age)` → `age` is the variable referring to the value 25.

- Common confusion: **VARIABLE vs. VALUE**

- **Variable**: The name/label that points to or references a value in memory (what Python does internally: creates a binding in the current namespace).
- **Value**: The actual data object stored in memory (what Python does internally: allocates memory for the object and stores its data).
- *Why confusing*: Beginners often think variables "contain" values like boxes, but variables are just names pointing to values.
- *Key difference*: Variables are identifiers you create; values are the data they refer to. Variables can be reassigned to point to different values, but the values themselves don't change unless modified.
- *Example*: In `x = 5`, `x` is the variable (a name), `5` is the value (an integer object). To tell which is happening: variables appear as names in code (like `x`, `age`), values appear as literals (like `5`, `"hello"`) or **expressions that evaluate to data**.

# Term: Name (variable name)
- Plain definition: A name is an identifier that binds to an object in Python's namespace, allowing you to reference and manipulate objects using meaningful labels.
- Why it matters: Names make code readable by abstracting away direct object references, enabling reuse and modification of data through symbolic identifiers.

- Example: `my_list = [1, 2, 3]; my_list.append(4)` → `my_list` is the name bound to the list object.

- Common confusion: **NAME vs. OBJECT**

- **Name**: The identifier/symbol you use in code (what Python does internally: stores a reference to an object in the current namespace dictionary).
- **Object**: The actual data structure in memory with its type, value, and identity (what Python does internally: creates and manages objects with reference counting and garbage collection).
- *Why confusing*: Beginners think names "hold" objects like containers, but names are just keys in a dictionary pointing to objects.
- *Key difference*: Names are user-defined symbols that can be reassigned; objects have persistent identity and can be shared by multiple names. Multiple names can refer to the same object.
- *Example*: In `a = [1, 2]; b = a`, both `a` and `b` are names referring to the same list object. To tell which is happening: names appear as identifiers (like `a`, `my_list`), objects are the underlying data (lists, strings, etc.) that names point to.

# Term: Namespace
- Plain definition: A namespace is a mapping (like a dictionary) that associates names with objects, providing isolated scopes where names can be defined and looked up without conflicts.
- Why it matters: Namespaces prevent name collisions and enable modular code by keeping different contexts separate (e.g., global vs. local variables).

- Example: In a function, `x = 5` creates a binding in the local namespace; outside the function, `x` might refer to something different in the global namespace.

- Common confusion: **NAMESPACE vs. SCOPE**

- **Namespace**: The actual dictionary-like structure that stores name-to-object mappings (what Python does internally: implements as a dict with fast lookups).
- **Scope**: The region of code where a namespace is accessible (what Python does internally: uses LEGB rule - Local, Enclosing, Global, Built-in - to resolve names across namespaces).
- *Why confusing*: Both relate to name resolution, but namespace is the storage mechanism while scope is the visibility rule.
- *Key difference*: Namespace is where bindings are stored; scope determines which namespaces are searched and in what order.
- *Example*: A function's local namespace stores its variables; the scope rules allow accessing global names if not shadowed locally. To tell which is happening: namespaces are the containers for bindings, scopes are the rules for accessing them.

# Term: Global Variable
- Plain definition: A global variable is a name defined at the module level (outside any function or class) that can be accessed from anywhere in the module, including inside functions.
- Why it matters: Global variables allow sharing data across different parts of a program, but they can make code harder to understand and debug if overused.

- Example: `count = 0; def increment(): global count; count += 1` → `count` is a global variable accessible everywhere in the module.

- Common confusion: **GLOBAL VARIABLE vs. LOCAL VARIABLE**

- **Global Variable**: Name bound in the global namespace (what Python does internally: stored in the module's `__dict__` and persists for the module's lifetime).
- **Local Variable**: Name bound in a function's local namespace (what Python does internally: created when the function is called and destroyed when it returns).
- *Why confusing*: Both are variables, but their accessibility and lifetime differ; beginners forget that functions create their own local scope.
- *Key difference*: Global variables are visible everywhere in the module; local variables are only visible inside their function and cease to exist after the function ends.
- *Example*: `x = 10` at module level is global; `x = 5` inside a function is local and doesn't affect the global `x`. To tell which is happening: check if the assignment is inside a function (local) or at module level (global); use `global` keyword to modify globals from inside functions.

---

# Term: Mutable

* **Plain definition:**
  A mutable object is a value that can be **changed in place after it is created**, without creating a new object.

* **Why it matters:**
  Mutability affects **how Python updates data**, **how variables behave when shared**, and **why changes sometimes appear “unexpected”**—especially in functions, loops, and compound assignments like `+=`.

---

* **Example:**
  `items = [1, 2]; items += [3]` → the list object is modified in place; `items` now refers to the **same list**, but with new contents.

---

* **Common confusion:** **MUTABLE vs. IMMUTABLE**

---

* **Mutable Object**:
  An object whose **contents can be changed without rebinding the name**.
  *(What Python does internally: the object stays in memory, and its internal state is updated; all references to that object see the change.)*

* **Immutable Object**:
  An object that **cannot be changed after creation**; any “change” creates a new object.
  *(What Python does internally: Python computes a new value and rebinds the name to a new object.)*

---

* **Why confusing:**
  Beginners think variables “store values” that change.
  In reality, **names point to objects**, and mutability determines whether Python **updates the object** or **creates a new one**.

---

* **Key difference:**
  Mutable objects can change **without rebinding** the variable name; immutable objects require **rebinding** to a new object.

---

* **Example:**
  `x = 10; x += 1` → `x` is immutable, so Python creates a new integer and rebinds `x`.
  `lst = [1, 2]; lst.append(3)` → `lst` is mutable, so Python changes the existing list.

---

* **How to tell which is happening:**
  Ask: *Can this object change internally?*

  * Numbers, strings, tuples → **immutable**
  * Lists, dicts, sets → **mutable**

  If multiple variables “see” the same change, you’re dealing with a **mutable object**.

---

### One-line mental model

**Mutability decides whether Python updates an object or replaces it with a new one.**

---

### excution jump commands

### _init_ method

used to setup a new object when it is first created.

For example, if you are making a Robot toy, __init__ is where you decide its name and what color it should be.

The "Self" Argument: The first part of __init__ is always self. This is like the robot pointing to itself to say, "These are my batteries and this is my name".
Setting Attributes: Its main job is to take information (like a name or age) and save it inside the object so it stays there.

### _hash_ vs _eq_

**__eq__(self, other): Equality**
defines the logic for the == operator.

**__hash__(self): Hashability**
returns an integer hash value used to "bin" objects in hash tables (like dict and set)

overriding __eq__ automatically makes a class unhashable (sets __hash__ to None). To make your custom object a dictionary key or a set member, you must implement both


