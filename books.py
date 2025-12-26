import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


csv_path = Path(__file__).parent / 'Bestsellers with categories.csv'
if not csv_path.exists():
	raise FileNotFoundError(f"CSV file not found: {csv_path}\nPlease place 'Bestsellers with categories.csv' next to books.py or update the filename.")

data = pd.read_csv(csv_path)
print(data.head(5))
print('\nColumn dtypes:\n', data.dtypes)
print('\nMissing values:\n', data.isnull().sum())


for col in ['Price', 'User Rating', 'Reviews', 'Year']:
	if col in data.columns:
		data[col] = pd.to_numeric(data[col], errors='coerce')


numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
print('\nNumeric columns to plot:', numeric_cols)

for col in numeric_cols:
	plt.figure(figsize=(6, 4))
	sns.boxplot(x=data[col])
	plt.title(f'Boxplot of {col}')
	plt.tight_layout()
	plt.show()


if 'Genre' in data.columns:
	genre_counts = data['Genre'].value_counts(dropna=True)
	if not genre_counts.empty:
		plt.figure(figsize=(6, 6))
		genre_counts.plot.pie(autopct='%1.1f%%', startangle=90, counterclock=False)
		plt.ylabel('')
		plt.title('Genre distribution')
		plt.tight_layout()
		plt.show()



numeric_df = data.select_dtypes(include=[np.number]).copy()
print('\nNumeric-only DataFrame (head):')
print(numeric_df.head())


numeric_df = numeric_df.dropna(axis=1, how='all')


if not numeric_df.empty:
	normalized_df = (numeric_df - numeric_df.min()) / (numeric_df.max() - numeric_df.min())
	print('\nMin-Max Normalized (head):')
	print(normalized_df.head())

	
	standardized_df = (numeric_df - numeric_df.mean()) / numeric_df.std(ddof=0)
	print('\nZ-score Standardized (head):')
	print(standardized_df.head())






