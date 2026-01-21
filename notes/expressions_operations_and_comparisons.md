

## Expressions & Operators

### One-Line Definition
An expression is anything Python can **evaluate to a value**.

---

### Why This Matters
Expressions are the **building blocks** of:
- conditions
- calculations
- decisions
- loops

If you don’t understand expressions, nothing else works.

---

### Core Operators
- Arithmetic: `+  -  *  /  //  %  **`
- Comparison: `==  !=  >  <  >=  <=`
- Logical: `and  or  not`

---

### Mental Model
Expressions are **questions** Python answers.

Example:
```python
age > 18
```
**Beginner Trap**
- Confusing = (assignment) with == (comparison).
- **Misunderstanding function behavior**: Assuming a function like show() can handle arbitrary data types and arguments, when it actually expects specific inputs (e.g., for visualization), leading to type or argument errors that break the pipeline.
- **Ignoring type dependencies**: Attempting operations (e.g., addition or multiplication) on incompatible types without checking, causing runtime failures instead of predictable results.
- **Overlooking operator precedence**: Expecting left-to-right evaluation in complex expressions, resulting in unexpected outcomes because Python follows mathematical rules (e.g., multiplication before addition).


#### Core Rules
- Expressions always evaluate to a value
- **Comparisons return booleans (Comparisons yield booleans with chaining )**: 
Equality and inequality checks produce True or False, and chained comparisons (e.g., a < b < c) are evaluated left-to-right, allowing concise but precise conditions.
- = assigns, == compares
- operations are type-sensitive