import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text = "The phone is amazing! Battery lasts long, camera quality is top-notch. However, it's a bit pricey"
tokens = word_tokenize(text)
print(tokens)
