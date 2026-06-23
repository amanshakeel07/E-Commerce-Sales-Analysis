import pandas as pd
df = pd.read_csv('/kaggle/input/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data/Amazon Sale Report.csv', low_memory=False)
columns_to_drop = ['index', 'Unnamed: 22']
columns_to_drop = [col for col in columns_to_drop if col in df.columns]
df = df.drop(columns=columns_to_drop)
df['Amount'] = df['Amount'].fillna(0)
df['Category'] = df['Category'].fillna('Unknown')
df['ship-city'] = df['ship-city'].fillna('Unknown')
df['ship-state'] = df['ship-state'].fillna('Unknown')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.to_csv('cleaned_amazon_sales.csv', index=False)
print("Data successfully cleaned! You can now download 'cleaned_amazon_sales.csv' from the right sidebar.")
print(f"Total clean rows: {df.shape[0]}")