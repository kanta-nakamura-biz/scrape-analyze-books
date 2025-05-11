import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSVファイルの読み込み
try:
    df = pd.read_csv('books_data.csv')
except FileNotFoundError:
    print("Error: books_data.csv not found. Please run scrape_books.py first.")
    exit()

# データの確認
print("\nLoaded Data Sample:")
print(df.head())
print("\nDataframe Information:")
print(df.info())

# 1. カテゴリー別の価格分析
plt.figure(figsize=(12, 6))
sns.boxplot(x='category', y='price', data=df)
plt.xlabel('Category')
plt.ylabel('Price (£)')
plt.title('Price Distribution by Category')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('price_by_category.png')
print("\nPrice distribution by category saved to price_by_category.png")

# 2. 価格と星評価の相関分析
plt.figure(figsize=(8, 6))
sns.scatterplot(x='rating', y='price', data=df)
plt.xlabel('Star Rating')
plt.ylabel('Price (£)')
plt.title('Price vs. Star Rating')
plt.grid(True)
plt.tight_layout()
plt.savefig('price_vs_rating.png')

# 相関係数を計算して表示
correlation = df['price'].corr(df['rating'])
print(f"Correlation between Price and Star Rating: {correlation:.2f}")
print("\nPrice vs. Star Rating saved to price_vs_rating.png")

print("\nData analysis complete. The results are saved as price_by_category.png and price_vs_rating.png.")