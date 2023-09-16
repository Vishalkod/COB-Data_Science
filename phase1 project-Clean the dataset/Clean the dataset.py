import pandas as pd

# Load the dataset
df = pd.read_csv('dataset - netflix1.csv')

# Handle Missing Values
# Assuming 'director', 'country', 'date_added', and 'rating' are the columns with missing values
df['director'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)

# Remove Outliers (assuming 'release_year' is the column you want to check for outliers)
q_low = df['release_year'].quantile(0.01)  # Adjust quantile as needed
q_high = df['release_year'].quantile(0.99)  # Adjust quantile as needed
df = df[(df['release_year'] >= q_low) & (df['release_year'] <= q_high)]

# Save the cleaned dataset
df.to_csv('cleaned_netflix_data.csv', index=False)
