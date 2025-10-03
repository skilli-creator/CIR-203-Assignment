import numpy as np

transactions = np.array([
    [1200, 1350, 1600, 1450, 1700, 1800],  # Branch 1
    [1500, 1550, 1650, 1720, 1850, 1900],  # Branch 2
    [1100, 1250, 1300, 1400, 1500, 1600],  # Branch 3
    [1800, 1750, 1850, 1900, 2000, 2100]   # Branch 4
])

print("Transaction Array (4x6):\n", transactions)


totals_per_branch = transactions.sum(axis=1)
print("\nTotal transactions per branch:", totals_per_branch)


highest_branch = np.argmax(totals_per_branch) + 1
print("Branch with highest transactions: Branch", highest_branch)


average_per_month = transactions.mean(axis=0)
print("Average monthly transactions across all branches:", average_per_month)


reshaped = transactions.reshape(3, 8)
print("\nReshaped Array (3x8):\n", reshaped)
print("\nImplication: Reshaping changes the structure but not the data. "
      "In this case, branch/month meaning is lost since data is rearranged "
      "into 3 rows and 8 columns without preserving branch-month relationships.")
