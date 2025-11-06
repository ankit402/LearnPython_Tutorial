import matplotlib.pyplot as plt
import numpy as np

#line plot
# x = [ 1,2,3,4,5]
# y= [1,4,9,16,25]
#
# plt.plot(x,y, color='red',linestyle='--', marker='o', linewidth=2)
# plt.xlabel('x Axis')
# plt.ylabel('y Axis')
# plt.title('Basic Plot')
# plt.figure(figsize=(9,5))
# plt.subplot(2,2,2)
# plt.show()

#bar plot

# categories = ['A', 'B', 'C', 'D', 'E', 'F']
#
# values = [10, 20, 30, 40, 50, 60]
#
# #create a bar plot
# plt.bar(categories, values, color='purple')
# plt.show()


# sewa_bill_year = [ 2021, 2022, 2023, 2024]
# sewa_bill_month = [ 'Jan', 'Feb', 'Mar' , 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# # Use lists (not sets) for consistent indexing
# bill_data = {
#     2021: [200, 400, 500, 300, 500, 200, 400, 700, 300, 700, 700, 300],
#     2022: [400, 600, 500, 300, 500, 200, 400, 700, 300, 700, 700, 300],
#     2023: [400, 500, 300, 500, 200, 400, 700, 300, 500, 300, 700, 300],
#     2024: [400, 600, 500, 300, 500, 400, 700, 300, 500, 400, 500, 300]
# }
# x = np.arange(len(sewa_bill_month))  # x locations for the groups
# width = 0.2  # width of the bars
#
# fig, ax = plt.subplots(figsize=(12, 6))
# # Plotting each year with offset
# for i, year in enumerate(sewa_bill_year):
#     ax.bar(x + i * width, bill_data[year], width, label=str(year))
#
# # Formatting
# ax.set_xlabel('Month')
# ax.set_ylabel('SEWA Bill Amount (AED)')
# ax.set_title('Monthly SEWA Bill Comparison (2021–2024)')
# ax.set_xticks(x + width * (len(sewa_bill_year) - 1) / 2)
# ax.set_xticklabels(sewa_bill_month)
# ax.legend()
# plt.tight_layout()
# plt.show()

x = [1,2,3,4,5]
y1= [1,4,9,16,25]
y2= [1,8,21,64,75]
plt.figure(figsize=(9,5))

plt.subplot(1,2,1)
plt.plot(x,y1, color='red')
plt.title('Plot 1')

plt.subplot(1,2,2)
plt.plot(x,y2, color='blue')
plt.title('Plot 2')

plt.subplot(2,2,3)
plt.plot(x,y1, color='green')
plt.title('Plot 3')

plt.subplot(2,2,4)
plt.plot(x,y1, color='purple')
plt.title('Plot 4')
plt.show()

