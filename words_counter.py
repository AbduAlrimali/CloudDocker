from collections import Counter
FILE_PATH = '/app/paragraphs-version2.txt'  

try:
    with open(FILE_PATH, 'r') as file:    
        content = file.read()
except FileNotFoundError as e:
    print(f"'{e}'")


def read_file(FILE_PATH):
    #Read a file and return its content as a list of lines.
    try:
        with open(FILE_PATH, 'r') as file:
            return file.readlines()
    except FileNotFoundError as e:
        print(f"'{e}'")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def count_words(lines):
    #Count the occurrences of each word in a list of lines.
    count_words = Counter()
    for line in lines:
        words = line.strip().split()
        normalized_words = [word.lower() for word in words]
        count_words.update(normalized_words)
    return count_words

def count_words_in_file(FILE_PATH):
    #Count the occurrences of each word in a file.
    lines = read_file(FILE_PATH)
    return count_words(lines)


word_counts = count_words_in_file(FILE_PATH)

print("Frequencies:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")
