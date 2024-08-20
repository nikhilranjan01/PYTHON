#implement the operation of extracting the word (feature) used in a sentence in py
#how can stopwords removal improve the quality of faeture in text-based machine lerning model in short
import nltk
from nltk import word_tokenize, pos_tag

# Download the necessary NLTK data files (only required once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_features(sentence, word_types):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    # Extract words that match the desired part-of-speech types
    features = [word for word, pos in tagged_words if pos in word_types]
    
    return features

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog."
word_types = ['NN', 'JJ']  # 'NN' for nouns, 'JJ' for adjectives
extracted_features = extract_features(sentence, word_types)

print("Extracted features:", extracted_features)
