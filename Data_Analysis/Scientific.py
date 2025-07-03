#calculate mean median or standard deviation of the array data
import numpy as np

arr_data =np.array([1,2,3,4,5])

#mean calculate
mean_data = np.mean(arr_data)
print("Mean for data: ", mean_data)

#median calculate
median_data = np.median(arr_data)
print("Median for data: ", median_data)

#standard deviation calculate
standard_deviation = np.std(arr_data)
print("Standard deviation for data: ", standard_deviation)