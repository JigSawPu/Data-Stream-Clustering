import random
import multiprocessing as m

samples = 2000000
n_tasks = 8

def sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1: return 1
    else: return 0
if __name__ == "__main__":
    p = m.Pool()
    results_async = [p.apply_async(sample) for i in range(n_tasks)]
    hits = sum(r.get() for r in results_async)
    pi = 4*hits/samples
    print(f'pi is {pi}')
