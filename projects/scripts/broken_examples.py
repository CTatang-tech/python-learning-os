# BE01 — Using a variable before assignment
print(total)
total = 100

# BE02 — Assuming later code runs after an error
print("Start")
1 / 0
print("End")   # never runs

# BE03 — Order matters
x = x + 1
x = 10

