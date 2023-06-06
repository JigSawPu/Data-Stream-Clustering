import multiprocessing as m
import time
import math

result_a = []
result_b = []
result_c = []

def calc_a(numbers):
    for nums in numbers:
        result_a.append(math.sqrt(nums**2))

def calc_b(numbers):
    for nums in numbers:
        result_b.append(math.sqrt(nums**2))

def calc_c(numbers):
    for nums in numbers:
        result_c.append(math.sqrt(nums**2))

if __name__ == "__main__":
    sample = list(range(5000000))

    p1 = m.Process(target=calc_a, args=(sample,))
    p2 = m.Process(target=calc_b, args=(sample,))
    p3 = m.Process(target=calc_c, args=(sample,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(end-start)

    start = time.time()
    calc_a(sample)
    calc_b(sample)
    calc_c(sample)
    end = time.time()
    print(end-start)
