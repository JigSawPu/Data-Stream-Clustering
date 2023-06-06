import numpy as np
import time
import multiprocessing

# class Process(multiprocessing.Process):
#     def __init__(self, matA, matB):
#         super(Process, self).__init__()
#         self.matA = matA
#         self.matB = matB
#     def run(self):
#         return np.dot(self.matA, self.matB)

# X = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Y = np.array([[4,3],[7,8],[2,2]])

# Example usage
np.random.seed(42)
N = 100
K = 3
means = np.array([[0, 0], [5, 5], [10, 0]])
cov = np.eye(2)
# this is a 3x1000 array of random multivariate normal distributions
X = np.vstack([np.random.multivariate_normal(mean, cov, int(N / K)) for mean in means])

p_parts = multiprocessing.cpu_count()
splitted_x = np.array_split(X, p_parts)

num_rows_in_X = X.shape[0]

if __name__ == '__main__':
    #by default no of processes = cpu count
    pool = multiprocessing.Pool()
    start_time = time.perf_counter()
    # assign one process for each splitted part
    # start processes in apply async
    #  maps function to its arguments
    processes = [pool.apply_async(np.dot, args=(splitted_x[i], X.T)) 
                 for i in range(p_parts)]
    # but get the results in sync in a list
    # use comprehension concat to get final result in <numpy.ndarray>
    result = np.concatenate([p.get() for p in processes])
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")