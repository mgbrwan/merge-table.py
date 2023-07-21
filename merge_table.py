import pandas as pd


df = pd.read_csv(r'/Users/mei/Desktop/L786.csv')
df2 = pd.read_csv(r'/Users/mei/Desktop/L133.csv')

# Merge two dataframes based on 'Gene name' and 'Gene_Symbol'
merged_df = pd.merge(df, df2, left_on='Gene name', right_on='Gene name', how='outer')

# Rename columns and reorder them
merged_df = merged_df.rename(columns={'Gene name': 'gene'})

# Print the merged dataframe
print(merged_df)

