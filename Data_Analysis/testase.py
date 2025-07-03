import pandas as pd

import pandas as pd

# Load only selected columns and top 100 rows
df = pd.read_excel('36905_MFKPROD_Updated.xlsx', usecols=['ID', 'PAN', 'SerNo', 'Status'], nrows=991104)
print("Original Data:\n", df)

# Filter for Success (assuming 1 = Success)
success_filter = df["Status"] == 1
success_df = df[success_filter]
print("\n✅ Success Cards:\n", success_df)
print("*********** Count of Success Cards ***********", len(success_df))

# Filter for Failed (assuming 0 = Failed)
failed_filter = df["Status"] == 0
failed_df = df[failed_filter]
print("\n❌ Failed Cards:\n", failed_df)
print("*********** Count of Failed Cards ***********", len(failed_df))

# Check for duplicate PANs (overall)
duplicate_counts = df['PAN'].value_counts()
duplicates = duplicate_counts[duplicate_counts > 1]
print("\n🔁 Repeated PANs and Their Counts:")
print(duplicates)

# Count how many times each PrintStatus value appears
print_status_counts = df['Status'].value_counts()

#count serno
serno = df['SerNo'].value_counts()
print("SerNo", serno)

df['SerNo_new']= df['SerNo'].apply(lambda x: x*2)

print("✅ Success count:", print_status_counts.get(1, 0))
print("❌ Failed count:", print_status_counts.get(0, 0))
# Write success results to file
with open('filtered_results.txt', 'w', encoding='utf-8') as f:
    f.write("✅ Success Cards:\n")
    f.write(success_df.to_string(index=False))
    f.write("\n\n❌ Failed Cards:\n")
    f.write(failed_df.to_string(index=False))
    f.write("\n\n🔁 Repeated PANs and Their Counts:\n")
    f.write(duplicates.to_string())
