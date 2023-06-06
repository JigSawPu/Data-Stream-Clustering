import random

samples = 1000000
hits = 0

for _ in range(samples):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
        hits += 1

pi = 4*hits/samples
print(f'pi is {pi}')