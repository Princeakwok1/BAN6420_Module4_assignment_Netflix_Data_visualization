Netflix Data Analysis - README

Overview

This project analyzes Netflix shows and movies using Python and R. The analysis involves:

Data Cleaning: Handling missing values.

Data Exploration: Summarizing the dataset.

Data Visualization: Creating charts using Python (Seaborn, Matplotlib) and R (ggplot2).

R Integration: Reproducing one visualization in R.

Step 1: Data Preparation

Files Included:

Netflix_shows_movies.csv – Original dataset.

Netflix_data_analysis.py – Python script for data analysis.

netflix_visualization.R – R script for visualization.

Netflix_shows_movies_cleaned.csv – Cleaned dataset (generated after running the Python script).

README.md – This document.

How to Run:

Ensure you have Python (>=3.7) and R installed.

Install required libraries:

pip install pandas numpy seaborn matplotlib

Run the Python script:

python Netflix_data_analysis.py

This will clean the dataset and save it as Netflix_shows_movies_cleaned.csv.

Step 2: Data Cleaning

Code Explanation:

import pandas as pd

# Load dataset
df = pd.read_csv("Netflix_shows_movies.csv")

# Display missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing categorical values
df = df.assign(
    director=df['director'].fillna("Unknown"),
    cast=df['cast'].fillna("Unknown"),
    country=df['country'].fillna("Unknown"),
    date_added=df['date_added'].fillna("Not Available")
)

# Drop rows where 'rating' is missing
df = df.dropna(subset=['rating'])

# Save cleaned dataset
df.to_csv("Netflix_shows_movies_cleaned.csv", index=False)

Expected Result:

The script will output the count of missing values before and after cleaning.

Saves the cleaned dataset as Netflix_shows_movies_cleaned.csv.

Step 3: Data Exploration

Code Explanation:

# Summary statistics
print(df.describe())

# Count unique values in 'type' column
print(df['type'].value_counts())

# Count unique genres
genres = df['listed_in'].str.split(', ').explode().value_counts()
print(genres.head(10))

Expected Result:

df.describe() gives a summary (e.g., mean, count, min, max) of numerical columns.

df['type'].value_counts() shows the count of Movies vs. TV Shows.

Top 10 genres are displayed.

Step 4: Data Visualization in Python

Code Explanation:

import matplotlib.pyplot as plt
import seaborn as sns

# Most watched genres
plt.figure(figsize=(10, 6))
genres.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Ratings distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['rating'], bins=10, kde=True)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

Expected Result:

Bar Chart of the top 10 most watched genres.

Histogram of ratings distribution.

Step 5: R Integration

How to Run the R Script:

Ensure you have R installed and the required libraries:

install.packages("ggplot2")
install.packages("dplyr")

Run the script in R:

source("netflix_visualization.R")

R Code Explanation:

library(ggplot2)
library(dplyr)

# Load cleaned dataset
df <- read.csv("Netflix_shows_movies_cleaned.csv")

# Process genres
genre_counts <- df %>%
  mutate(listed_in = strsplit(as.character(listed_in), ",")) %>%
  unnest(listed_in) %>%
  mutate(listed_in = trimws(listed_in)) %>%
  count(listed_in, sort = TRUE) %>%
  top_n(10, n)

# Bar chart for most watched genres
ggplot(genre_counts, aes(x = reorder(listed_in, n), y = n, fill = listed_in)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  theme_minimal() +
  labs(title = "Top 10 Most Watched Genres on Netflix",
       x = "Genre",
       y = "Number of Titles") +
  theme(legend.position = "none")

Expected Result:

Bar chart of the top 10 genres, similar to Python's output.# BAN6420_Module4_assignment_Netflix_Data_visualization
