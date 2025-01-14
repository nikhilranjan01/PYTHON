from collections import Counter
stop_words = {'the', 'a', 'is'}

def clean_text(text):
    text = text.lower()
    words = ''.join(char if char.isalnum() else ' ' for char in text).split()
    words = [word for word in words if word not in stop_words]
    return words

def word_frequency(text):
    words = clean_text(text)
    return Counter(words)

if __name__ == "__main__":
    text = "A is the first letter of the alphabet..B is the second letter of the alphabet"
    freq = word_frequency(text)
    print(freq.most_common())