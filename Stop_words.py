import spacy
from spacy.lang.en.stop_words import STOP_WORDS # -------------------# Import the predefined list of stop words from SpaCy

#----------------# Load the English SpaCy model with its pre-built NLP pipeline
nlp = spacy.load("en_core_web_sm")#--------------------  # This pipeline includes tokenization, part-of-speech tagging, etc.

#--------------------# Create a document using the SpaCy pipeline
doc = nlp("we just opened our shop, the selling part is coming soon")

#----------------# Iterate through tokens (words) in the document
for word in doc:# -------------------- # Loop to check if each word in the document is a stop word
    if word.is_stop: #------------------ # If the word is a stop word, print it with an asterisk for distinction
        print(word, "*")

#------------------------# Define a function to preprocess text by removing stop words and punctuation
def preprocessing(text):
   # -------------------# Create a SpaCy document for the input text
    doc = nlp(text)
    
   #----------------- # List comprehension to filter out stop words and punctuation




    no_stop_words = [
        token.text #------------------ # Extract the text of the token
        for token in doc # ----------------# Iterate through all tokens in the document
        if not token.is_stop and not token.is_punct  #---------------# Exclude stop words and punctuation
    ]
    
    return no_stop_words  # Return the processed list of words
    return " ".join(no_stop_words) # to get a string out of seperate words by joining them


Example Usage #--------------------
text = "This is an example sentence to demonstrate text preprocessing."
print(preprocessing(text))
#-------------------# Output: ['example', 'sentence', 'demonstrate', 'text', 'preprocessing']



########################################################################

Removing stop words and lemmatizing words in (bag of n grams/bag of words)


from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer(ngram_range=(1, 3)) # if we write (1 ,1) then it will generate words of length 1 and if we write (1 ,2) then it will generate 
# words of length from 1 to 2 we have words of length 2 only if we gave (2 ,2) as argument
v.fit(["thor is looking for a job"])
v.vocabulary_

corpus = [
    "thor ate pizza",  # Missing comma added here
    "thor is tall",
    "loki ate pizza"
]

import spacy
nlp = spacy.load("en_core_web_sm")  # Load SpaCy pipeline

# Define the preprocess function to clean and lemmatize the input text
def preprocess(text):
    doc = nlp(text)  # Create a SpaCy doc from the input text
    filtered_words = []  # Initialize an empty list for filtered words
    
    for token in doc:  # Iterate over each token in the text
        # Skip tokens that are stop words or punctuation
        if token.is_stop or token.is_punct:
            continue
        # Add lemmatized form of the token to the list
        filtered_words.append(token.lemma_)
    
    # Return the processed text as a single string
    return " ".join(filtered_words)

for i in range(0,len(corpus),1):
    print(preprocess(corpus[i]))

    # both above and below line will give same output below one is list compreghension

corpus_processed = [preprocess(text) for text in corpus]
corpus_processed # type = list

#now that we have process text we are going to use count vectorizer
v = CountVectorizer(ngram_range = (1,2))
v.fit(corpus_processed) # fit required list as an argument
v.vocabulary_ # type dict 
# where 'thor' is value and 6 is like a key

v.transform(["thor eat pizza"]).toarray() #we converted text into vector then we 
converted then we converted that vector to an array

v.transform(["hulk eat pizza"]).toarray() # if the words are not in vocabulary then  we will face OOV Error 
# (out-of-vocabulary)
