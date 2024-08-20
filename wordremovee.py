#implement the operation of extracting the word (feature) used in a sentence in python without using library
def extract_words(sentence):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_sentence = ""
    for char in sentence:
        if char not in punctuation:
            cleaned_sentence += char
            words = cleaned_sentence.splite()
            
            return words
        sentence ="jiet group @ of  institution depatment Aiml."
        words = extract_words(sentence)
        print(words)
        
    

