import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Netflix_shows_movies.csv")  

# ============================
# STEP 2a: CHECK MISSING VALUES (Before Cleaning)
# ============================
print("Missing values before cleaning:")   #print the missing values before cleaning
print(df.isnull().sum())

# ============================
# STEP 2b: DATA CLEANING
# ============================
# Fill missing categorical values
df = df.assign(
    director=df['director'].fillna("Unknown"),
    cast=df['cast'].fillna("Unknown"),
    country=df['country'].fillna("Unknown"),
    date_added=df['date_added'].fillna("Not Available")
)

# Drop rows where 'rating' is missing
df = df.dropna(subset=['rating'])

# ============================
# STEP 3: CHECK MISSING VALUES (After Cleaning)
# ============================
print("\nMissing values after cleaning:")         #print missing values after cleaning
print(df.isnull().sum())

# ============================
# STEP 4: DATA EXPLORATION
# ============================

# Summary statistics
print("\nSummary Statistics (Numerical Columns):")      # Print summary statistics Numerical columns
print(df.describe())

print("\nSummary Statistics (Categorical Columns):")     # Print summary statistics Categorical columns
print(df.describe(include='object'))

# Count unique genres
unique_genres = set(genre.strip() for sublist in df['listed_in'].dropna().str.split(',') for genre in sublist)
print(f"\nNumber of unique genres: {len(unique_genres)}")     # Print Number of Unique genres
print(f"Unique genres: {unique_genres}")                      # Print the Unique genres

# Count Movies vs. TV Shows
print("\nCount of Movies vs. TV Shows:")
print(df['type'].value_counts())

# ============================
# STEP 5: DATA VISUALIZATION
# ============================

# 📊 1️⃣ Most Watched Genres (Bar Chart)
plt.figure(figsize=(12, 6))
genre_counts = df['listed_in'].str.split(',').explode().str.strip().value_counts().head(10)  # Top 10 genres
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
plt.title("Top 10 Most Watched Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()

# 📊 2️⃣ Ratings Distribution (Histogram)
plt.figure(figsize=(10, 5))
sns.histplot(df['rating'], bins=10, kde=True, palette="coolwarm")
plt.title("Distribution of Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# 📊 3️⃣ Ratings Distribution (Boxplot)
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['rating'], palette="pastel")
plt.title("Boxplot of Netflix Ratings")
plt.xlabel("Rating")
plt.xticks(rotation=45)
plt.show()


# Save the cleaned dataset for R analysis
df.to_csv("Netflix_shows_movies_cleaned.csv", index=False)

