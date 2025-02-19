# Split genres and count occurrences
genre_counts <- df %>%
  mutate(listed_in = strsplit(as.character(listed_in), ",")) %>%
  unnest(listed_in) %>%
  mutate(listed_in = trimws(listed_in)) %>%  # Remove spaces
  count(listed_in, sort = TRUE) %>%
  top_n(10, n)  # Get top 10 genres

# Bar Chart for Most Watched Genres
ggplot(genre_counts, aes(x = reorder(listed_in, n), y = n, fill = listed_in)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  theme_minimal() +
  labs(title = "Top 10 Most Watched Genres on Netflix",
       x = "Genre",
       y = "Number of Titles") +
  theme(legend.position = "none")
