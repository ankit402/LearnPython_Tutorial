#"### Assignment 8: Fancy Indexing and Boolean Indexing\n",

#"1. Create a NumPy array of shape (5, 5) filled with random integers.
# Use fancy indexing to extract the elements at the corners of the array.\n",
#2. Create a NumPy array of shape (4, 4) filled with random integers.
# Use boolean indexing to set all elements greater than 10 to 10.\n",

import numpy as np
np_array= np.random.randint(1,40, size=(4,4))
print("Original array:\n", np_array)
np_array[np_array > 10] = True
print("\nModified array:\n", np_array)
