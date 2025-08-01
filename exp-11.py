import matplotlib.pyplot as plt
import numpy as np
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [5000, 7000, 8000, 7500, 9000, 12000, 15000, 14000, 16000, 17000, 18000, 20000]
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)
plt.title("Monthly Sales Trend (Line Plot)", fontsize=14)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10, 5))
plt.scatter(months, sales, color='red', edgecolor='black', s=100)
plt.title("Monthly Sales Data (Scatter Plot)", fontsize=14)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='skyblue', edgecolor='black')
plt.title("Monthly Sales Data (Bar Plot)", fontsize=14)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.xticks(rotation=45)
plt.show()

