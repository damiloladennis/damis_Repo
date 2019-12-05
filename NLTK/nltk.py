import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
# Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
#Lexicon Normalization
#performing stemming and Lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens=nltk.word_tokenize(sent)
print(tokens)

lem = WordNetLemmatizer()
stem = PorterStemmer()

word = "flying"
print("Lemmatized Word:",lem.lemmatize(word,"v"))
print('\n')
print("Stemmed Word:",stem.stem(word))
print('\n')

stop_words=set(stopwords.words("english"))
print(stop_words)
print('\n')

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""

tokenized_text=sent_tokenize(text)
tokenized_word=word_tokenize(text)
fdist = FreqDist(tokenized_word)

fdist.plot(30,cumulative=False)
plt.show()

filtered_sent=[]
for w in tokenized_text:
    if w not in stop_words:
        filtered_sent.append(w)


print("Filtered Sentence:",filtered_sent)
print('\n')

print("Tokenized Sentence:",tokenized_text)
print('\n')
print("Filtered Sentence:",filtered_sent)

print('\n')
print(tokenized_text)
print('\n')
print(tokenized_word)
print('\n')
print(fdist)