import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

class TextProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def read_text_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()
            return text
        except FileNotFoundError as e:
            print(f'"{e}"')
            return None
        except Exception as e:
            print(f'Error: {e}')
            return None

    def remove_stop_words_and_punctuations(self, text):
        if text is None:
            return None
        try:
            words = word_tokenize(text)
            stopWords = set(stopwords.words('english'))
            punctuations = set(string.punctuation)
            filteredWords = [word for word in words if word.lower() not in stopWords and word not in punctuations]
            filteredText = ' '.join(filteredWords)
            return filteredText
        except Exception as e:
            print(f'{e}')
            return None

    def save_filtered_text(self, filtered_text, output_file_path):
        if filtered_text is None:
            print("Error: filtered text is none. cannot write to file.")
            return None
        try:
            with open(output_file_path, 'w') as output_file:
                output_file.write(filtered_text)
                print(f"Filtered text has been saved to {output_file_path}.")
        except Exception as e:
            print(f"Error saving filtered text to file: {e}")


if __name__ == "__main__":
    input_file_path = 'D:\\College\\Subjects\\Y2 - Semester 2\\Cloud Computing\\assignments\\Docker\\paragraphs.txt'
    output_file_path = 'D:\\College\\Subjects\\Y2 - Semester 2\\Cloud Computing\\assignments\\Docker\\paragraphs-version2.txt'

    processor = TextProcessor()
    text = processor.read_text_file(input_file_path)
    filtered_text = processor.remove_stop_words_and_punctuations(text)
    processor.save_filtered_text(filtered_text, output_file_path)
