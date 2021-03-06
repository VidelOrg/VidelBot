import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import LatentDirichletAllocation
import sys

def setup():
    from nltk import download
    #download wordnet
    download("wordnet")

#Use text in file_address and find most important topics
def topic_lists(file_address):
    lemm = WordNetLemmatizer()
    class LemmaCountVectorizer(CountVectorizer):
        def build_analyzer(self):
            analyzer = super(LemmaCountVectorizer, self).build_analyzer()
            return lambda doc: (lemm.lemmatize(w) for w in analyzer(doc))


    with open(file_address, 'r') as file:
        data = file.read().replace('\n', '')

    text = [data]
    count_vect = LemmaCountVectorizer(stop_words='english')
    doc_term_matrix = count_vect.fit_transform(text)


    LDA = LatentDirichletAllocation(n_components=5, random_state=42,learning_method = 'online',
                                    learning_offset = 50.,)
    LDA.fit(doc_term_matrix)
    first_topic = LDA.components_[0]
    top_topic_words = first_topic.argsort()[-10:]
    for i in top_topic_words:
        print(count_vect.get_feature_names()[i])

    topic_lists = []
    for i,topic in enumerate(LDA.components_):
        topic_lists.append([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print("topic_lists:", topic_lists)
    return topic_lists

if __name__ == "__main__":
    topic_lists()