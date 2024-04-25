import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding ='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f'Error: file "{file_path}" not found')
        return None
    except Exception as e:
        print(f'Error: reading file: {e}')
        return None

def remove_stop_words_and_punctuations(text):
    if text is None:
        return None
    try:
        words = word_tokenize(text)

        english_stop_words = set(stopwords.words('english'))

        punctuation = set(string.punctuation)

        filtered_words = [word for word in words if word.lower() not in english_stop_words and word not in punctuation]

        filtered_text = ' '.join(filtered_words)

        return filtered_text
    except Exception as e:
        print(f'Error removing stop words and punctuations: {e}')
        return None

def save_filtered_text(filtered_text, output_file_path):
    if filtered_text is None:
        print("Error: filtered text is none. cannot write to file.")
        return None
    
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(filtered_text)
            print(f"Filtered text has been saved to {output_file_path}.")
    except Exception as e:
        print(f"Error saving filtered text to file: {e}")

input_file_path = 'D:\\College\\Subjects\\Y2 - Semester 2\\Cloud Computing\\assignments\\Docker\\paragraphs.txt'
output_file_path = 'D:\\College\\Subjects\\Y2 - Semester 2\\Cloud Computing\\assignments\\Docker\\paragraphsv2.txt'

text = read_text_file(input_file_path)

filtered_text = remove_stop_words_and_punctuations(text)

save_filtered_text(filtered_text, output_file_path)