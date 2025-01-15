import string

def tokenize_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return tokens

input_text = "The phone is amazing! Battery lasts long, camera quality is top-notch. However, it's a bit pricey"
tokens = tokenize_text(input_text)
print("Tokens:", tokens)  
