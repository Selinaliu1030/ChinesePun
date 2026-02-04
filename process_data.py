import pandas as pd

# Read the CSV file
df = pd.read_csv('./data/punes_list_clean.csv')

# Add a new column called 'label' filled with 1
df['label'] = 1
df['id'] = range(len(df))

# Save the updated CSV file
df.to_csv('./data/punes_list_clean_test.csv', index=False)

print(f"✅ Successfully added 'label' column with value 1")
print(f"Total rows: {len(df)}")
print(f"\nFirst few rows:")
print(df.head())

# Read another CSV file
df2 = pd.read_csv('./data/no_puns_clean.csv')

## add id column
df2['id'] = range(len(df), len(df) + len(df2))
df2['label'] = 0

# Save the updated CSV file
df2.to_csv('./data/no_puns_clean.csv', index=False)

print(f"✅ Successfully added 'id' column with values {len(df)} to {len(df2) + len(df) - 1}")
print(f"Total rows: {len(df2)}")
print(f"\nFirst few rows:")
print(df2.head())

# Merge the two dataframes
merged_df = pd.concat([df, df2], ignore_index=True)
merged_df.to_csv('./data/combined_pun_nonpun.csv', index=False)