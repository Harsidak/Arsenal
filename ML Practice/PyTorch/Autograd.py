import torch as t

# --- STEP 1: START THE RECORDING ---
# By default, tracking is False. Setting requires_grad=True tells PyTorch
# to build a math map for this specific tensor.
x = t.tensor(3.0, requires_grad=True)

# --- STEP 2: THE FORWARD PASS & FOOTPRINTS ---
y = x**2

print(x) # Output: tensor(3., requires_grad=True)
print(y) # Output: tensor(9., grad_fn=<PowBackward0>)
# 'grad_fn' is the receipt. It proves PyTorch tracked the squaring operation 
# and knows exactly how to calculate its derivative later.

# --- STEP 3: REWINDING THE GRAPH (.backward) ---
# This executes the calculus and stores the result directly in the source tensor's .grad property
y.backward()
print(x.grad) # Output: tensor(6.) -> d/dx of x^2 is 2x. Plug in 3: 2*(3) = 6.


# --- STEP 4: THE CHAIN RULE (MULTIPLE LAYERS) ---
# Resetting x for a fresh, clean graph demonstration
x = t.tensor(3.0, requires_grad=True)

y = x**2
z = t.sin(y) # Layering a second function on top

z.backward() 
print(x.grad) # Output: tensor(-0.989992)


# --- STEP 5: TURNING OFF THE RECORDER (INFERENCE MODE) ---
# Peer check: assigning 'x = t.no_grad()' will just overwrite your data with a function object.
# To freeze tracking for a block of code, use the 'with' context manager like this:
with t.no_grad():
    inference_y = x ** 2 # No graph built here. Zero VRAM overhead.