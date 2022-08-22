import streamlit as st
import numpy as np
import spacy
import sklearn
import string
# python -m spacy download en_core_web_sm
@st.cache
def download_spacy():
    # Fetch data from URL here, and then clean it up.
    spacy.cli.download("en_core_web_sm")

download_spacy()


# nlp = spacy.load("en_core_web_sm-3.0.0\en_core_web_sm-3.0.0")
nlp = spacy.load("en_core_web_sm")
stop_words = nlp.Defaults.stop_words
punctuations = string.punctuation


def spacy_tokenizer(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    doc = nlp(sentence)

    # print(doc)

    # Lemmatizing each token and converting each token into lowercase
    mytokens = [ word.lemma_.lower().strip() for word in doc ]

    # print(mytokens)

    # Removing stop words
    mytokens = [ word for word in mytokens if word not in stop_words and word not in punctuations ]

    # return preprocessed list of tokens
    return mytokens
import re
def clean_text(text):
    text = re.sub("-", " ", text)
    text = re.sub('"', " ", text)
    text = re.sub("\[.*?\]", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = " ".join(filter(lambda x: x[0] != "@", text.split()))
    return text

# st.write(model)

user_input = st.text_area('Enter text')
button = st.button("Predict")




if user_input and button :
    # test_sample
    doc=nlp([user_input])
    doc=clean_text(doc)
    if doc.ent_type_=="GPE":
        st.write("It is City")
    if doc.ent_type_=='PERSON':
        st.write('Person')
    else:
        st.write('Neither city nor Person')

