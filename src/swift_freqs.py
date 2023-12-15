import pandas as pd
from collections import Counter
import string

# Read the CSV file into a pandas DataFrame
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found!")
        return None

# Function to clean and tokenize the text
def clean_and_tokenize(text):
    # Convert text to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text
    tokens = text.split()
    return tokens

# Function to generate word frequency CSV sorted by frequency
def generate_word_frequency_csv(data, column, output_file):
    words = []
    for _, row in data.iterrows():
        words.extend(clean_and_tokenize(row[column]))

    word_freq = Counter(words)
    # Sort words by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    
    df_word_freq = pd.DataFrame(sorted_word_freq.items(), columns=['Word', 'Frequency'])
    df_word_freq.to_csv(output_file, index=False)
    print(f"Word frequency CSV generated: {output_file}")

file_path = '../data/swift.csv'

swift_data = read_csv(file_path)

if swift_data is not None:
    # Generate word frequency CSV for titles
    generate_word_frequency_csv(swift_data, 'Title', '../data/title_word_frequency.csv')

    # Generate word frequency CSV for lyrics
    generate_word_frequency_csv(swift_data, 'Lyrics', '../data/lyrics_word_frequency.csv')
