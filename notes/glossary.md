# Term: Updating
- Plain definition: Updating means replacing a variable's old value with a new value.
- Why it matters: You need to know that when you update, the old value is **gone forever**—it doesn't exist alongside the new value.
- Example: `X = 5; X = 10` → X is now 10, not "both 5 and 10"
- Common confusion: **UPDATING vs. REASSIGNMENT**
  - **Reassignment**: Technical term for the mechanism (using `=` to bind a new value to a name)
  - **Updating**: Emphasizes that we're *changing* an existing variable that already has a value
  - *Why confusing*: Both use `=` and both change the variable
  - *Key difference*: Reassignment is the HOW (the syntax/mechanism), updating is the WHY/CONTEXT (we're modifying something that existed before)


# Term: Rebinding
- Plain definition: Rebinding means making a name point to a different value (redirecting the label to something new).
- Why it matters: Helps you understand that variables are *names for values*, not containers. You're changing which value the name points to, not modifying the value itself.
- Example: `X = 5; X = 10` → The name X now points to 10 instead of 5
- Common confusion: **REBINDING vs. REFERENCE**
  - **Reference**: Means "pointing to" or "using" a value; just *reading* what a name points to (no change)
  - **Rebinding**: Means *changing* what a name points to; actively breaking the old connection and creating a new one
  - *Why confusing*: Both involve names pointing to values, so they seem similar
  - *Key difference*: Reference is **static/read-only** (just accessing the current value), rebinding is **dynamic/changing** (breaking and remaking the connection)
  - *Example*: `y = X + 2` creates a **reference** to X (reads its value). `X = 10` **rebinds** X (changes what it points to)

# Term: Traceback
- Plain definition: A traceback is a map showing the path Python took through your code before hitting an error.
- Why it matters: It tells you *where* the error happened and *how it got there*, making debugging possible instead of guessing.
- Example: Shows `Cell In[12], line 2` → `age + "years"` so you know exactly which line broke
- Common confusion: **TRACEBACK vs. ERROR MESSAGE**
  - **Error Message**: The **final verdict** — the type and description of what went wrong
  - **Traceback**: The **entire map/path** showing how Python got to the error
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


