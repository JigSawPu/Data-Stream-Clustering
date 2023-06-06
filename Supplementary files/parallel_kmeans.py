import numpy as np
import multiprocessing

class KMeans_parallel:
    '''Initialize the class with default k and max_iter.'''
    def __init__(self, k=2, max_iter=50):
        self.k = k
        self.max_iter = max_iter

    def fit(self, X):
        '''This function uses k means algorithm to fit the input dataset'''
        # Set the initial centroids to randomly selected points in data
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        p_parts = multiprocessing.cpu_count()
        splitted_x = np.array_split(X, p_parts)
        for i in range(self.max_iter):
            # Calculate the distance of all instances from all the cluster
            # Set label of each instance based on their distance from the nearest cluster
            pool = multiprocessing.Pool()
            processes = [pool.apply_async(self.assign_labels_by_distance, 
                                          args=(splitted_x[i], self.centroids)) 
                                          for i in range(p_parts)]
            self.labels = np.concatenate([p.get() for p in processes])
            # For instances in same cluster, calculate their centroid and update 
            for j in range(self.k):
                self.centroids[j] = X[self.labels == j].mean(axis=0)

    def assign_labels_by_distance(self, X_p, centroids):
        l2_squared = ((X_p - centroids[:, np.newaxis])**2).sum(axis=2)
        labels = np.argmin(l2_squared, axis=0)
        return labels

    def predict(self, X):
        '''This function is used to predict the label of test set by calculating the
        distance from the nearest cluster'''
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def __str__(self) -> str:
        return f'K means models with parameters: \nk: {self.k}, max_iter: {self.max_iter}'
    

# Example usage
if __name__ =="__main__":
    np.random.seed(42)
    N = 10000
    K = 3
    means = np.array([[0, 0], [5, 5], [10, 0]])
    cov = np.eye(2)
    # this is a K by N array of random multivariate normal distributions
    X = np.vstack([np.random.multivariate_normal(mean, cov, int(N / K)) for mean in means])

    kmeans = KMeans_parallel(k=4)
    kmeans.fit(X)
    print(f'The centroids of clusters are:\n {kmeans.centroids}\n')
