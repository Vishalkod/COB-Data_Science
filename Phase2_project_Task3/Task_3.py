import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('dataset - netflix1.csv')

# Check the first few rows
print(data.head())

# Show Types Count
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=data)
plt.title('Distribution of Show Types')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Top Countries with Most Shows
top_countries = data['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries with Most Shows')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()

# Release Year Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['release_year'], kde=True)
plt.title('Release Year Distribution')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()

# Rating Distribution
rating_counts = data['rating'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribution of Ratings')
plt.axis('equal')
plt.show()
