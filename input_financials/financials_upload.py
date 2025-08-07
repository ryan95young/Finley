import pandas as pd

# Load Excel file
df = pd.read_excel("financials.xlsx")

# Print the summary
print(grouped[["Actual", "Budget", "Variance"]])