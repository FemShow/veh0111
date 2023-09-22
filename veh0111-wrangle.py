import pandas as pd

# Define the file path
file_path = "/Users/femisokoya/Documents/GitHub/veh0111/veh0111.xls"

# Define the worksheet name
sheet_name = "VEH0111"

# Read the Excel file, skip the first 4 rows, and use row 5 as column headers
df = pd.read_excel(file_path, sheet_name=sheet_name, header=4)

# Save the DataFrame to veh0111-result.csv
df.to_csv("veh0111-result.csv", index=False)

print("Data frame saved to veh0111-result.csv")
