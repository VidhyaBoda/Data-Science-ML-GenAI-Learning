# 12 - Loops and Iterations

state = {
    "attempt": 0,
    "max_attempts": 3,
    "quality": 0.0
}

while state["attempt"] < state["max_attempts"] and state["quality"] < 0.9:
    state["attempt"] += 1
    state["quality"] += 0.35
    print(f"Attempt {state['attempt']}: quality={state['quality']:.2f}")

print("Final state:", state)
