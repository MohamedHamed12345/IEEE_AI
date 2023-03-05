


```python
import numpy as np

# 1. np.array(): Creates a new numpy array from a Python list or tuple.
arr = np.array([1, 2, 3, 4])

# 2. np.arange(): Creates a new numpy array with a range of values.
arr = np.arange(0, 10, 2)

# 3. np.zeros(): Creates a new numpy array filled with zeros.
arr = np.zeros((3, 3))

# 4. np.ones(): Creates a new numpy array filled with ones.
arr = np.ones((2, 4))

# 5. np.full(): Creates a new numpy array filled with a specific value.
arr = np.full((3, 3), 5)

# 6. np.eye(): Creates a new numpy identity matrix.
arr = np.eye(3)

# 7. np.diag(): Extracts the diagonal from a numpy array or creates a new numpy array with a diagonal.
arr = np.array([[1, 2], [3, 4]])
diag = np.diag(arr)

# 8. np.transpose(): Transposes a numpy array.
arr = np.array([[1, 2], [3, 4]])
arr_transpose = np.transpose(arr)

# 9. np.reshape(): Reshapes a numpy array.
arr = np.arange(12)
new_arr = np.reshape(arr, (3, 4))

# 10. np.ravel(): Flattens a numpy array.
arr = np.array([[1, 2], [3, 4]])
flattened_arr = np.ravel(arr)

# 11. np.concatenate(): Concatenates two or more numpy arrays.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2))

# 12. np.split(): Splits a numpy array into multiple sub-arrays.
arr = np.array([1, 2, 3, 4, 5, 6])
sub_arrs = np.split(arr, 3)

# 13. np.max(): Returns the maximum value in a numpy array.
arr = np.array([1, 2, 3, 4, 5])
max_val = np.max(arr)

# 14. np.min(): Returns the minimum value in a numpy array.
arr = np.array([1, 2, 3, 4, 5])
min_val = np.min(arr)

# 15. np.mean(): Computes the mean of a numpy array.
arr = np.array([1, 2, 3, 4, 5])
mean_val = np.mean(arr)

# 16. np.median(): Computes the median of a numpy array.
arr = np.array([1, 2, 3, 4, 5])
median_val = np.median(arr)

# 17. np.std(): Computes the standard deviation of a numpy array.
arr = np.array([1, 2, 3, 4, 5])
std_val = np.std(arr)

# 18. np.var(): Computes the variance of a numpy array.
arr = np.array([1, 2, 3, 4, 5])
var_val = np.var(arr)

# 19. np.dot(): Computes the dot product of two numpy arrays.
arr1 = np.array([1, 2


# 20. np.clip(): Clips (limits) the values in a numpy array to a specified range.
arr = np.array([1, 2, 3, 4, 5])
clipped_arr = np.clip(arr, 2, 4)

# 21. np.sort(): Sorts the values in a numpy array.
arr = np.array([3, 1, 4, 2, 5])
sorted_arr = np.sort(arr)

# 22. np.argsort(): Returns the indices that would sort a numpy array.
arr = np.array([3, 1, 4, 2, 5])
sorted_indices = np.argsort(arr)

# 23. np.unique(): Returns the unique values in a numpy array.
arr = np.array([1, 2, 3, 2, 1])
unique_vals = np.unique(arr)

# 24. np.bincount(): Counts the number of occurrences of each value in a numpy array of non-negative integers.
arr = np.array([0, 1, 2, 2, 1, 1])
count_arr = np.bincount(arr)

# 25. np.random.rand(): Generates a numpy array with random values between 0 and 1.
rand_arr = np.random.rand(3, 2)

# 26. np.random.randn(): Generates a numpy array with random values from a standard normal distribution (mean 0, variance 1).
randn_arr = np.random.randn(3, 2)

# 27. np.random.randint(): Generates a numpy array with random integer values in a specified range.
randint_arr = np.random.randint(0, 10, (3, 2))

# 28. np.random.choice(): Generates a random sample from a given 1-D numpy array.
arr = np.array([1, 2, 3, 4, 5])
sample = np.random.choice(arr, size=3, replace=False)

# 29. np.random.shuffle(): Shuffles the values in a numpy array in place.
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)