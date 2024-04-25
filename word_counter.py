import os
from nltk.corpus import stopwords
from collections import Counter

file_path = '/app/filtered-paragraphs.txt'  

try:
    with open(file_path, 'r', encoding='utf-8') as file:    
        content = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

def count_words_in_file(file_path):
    word_counts = Counter()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Tokenize the line into words (split by whitespace)
            words = line.strip().split()
            # Normalize words (convert to lowercase, remove punctuation, etc.)
            normalized_words = [word.lower() for word in words]
            # Update the word counts using Counter
            word_counts.update(normalized_words)
    return word_counts


word_counts = count_words_in_file(file_path)

print("Word Frequencies:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")
