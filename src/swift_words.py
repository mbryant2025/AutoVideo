import pandas as pd

file_path = 'data/swift.csv'



# Read the CSV file into a pandas DataFrame
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found!")
        return None
    
swift_data = read_csv(file_path)

# Function to search for songs with a given word in their title
def search_title(data, word):
    matching_songs = data[data['Title'].str.contains(word, case=False)]
    return matching_songs[['Title', 'Album']]

# Function to search for songs with a given word in their lyrics
def search_lyrics(data, word):
    matching_lyrics = data[data['Lyrics'].str.contains(word, case=False)]
    return matching_lyrics[['Title', 'Album', 'Lyrics']]

# Function to print specific lines from lyrics containing the word
def lyrics_with_word(lyrics, word):
    lines_with_word = [line.strip() for line in lyrics.split('\n') if word.lower() in line.lower()]
    return lines_with_word    

def find_titles(word):
    matching_title_songs = search_title(swift_data, word)
    # Return just the titles as a list
    return matching_title_songs['Title'].tolist()

def find_lyrics(word):
    matching_lyrics_songs = search_lyrics(swift_data, word)
    # Return just the titles as a list as well as the line that the word appears in
    titles = matching_lyrics_songs['Title'].tolist()
    lyrics = matching_lyrics_songs['Lyrics'].tolist()
    lines_with_word = [lyrics_with_word(lyric, word) for lyric in lyrics]
    return list(zip(titles, lines_with_word))


def main(word_in_title, word_in_lyrics):

    print("Songs with the word '{}' in the title:".format(word_in_title))
    matching_title_songs = find_titles(word_in_title)
    print(matching_title_songs)

    print("\nSongs with the word '{}' in the lyrics:".format(word_in_lyrics))
    matching_lyrics_songs = find_lyrics(word_in_lyrics)
    print(matching_lyrics_songs)


if __name__ == '__main__':
    main('love', 'science')
