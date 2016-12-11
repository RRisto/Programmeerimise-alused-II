# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:15:58 2016

@author: Risto
"""

from twython import Twython
twitter = Twython('C8Jpl39xJIVC6uw4zb6Rj809s','VjTKEep9JMmrk8mezvSF3C4igtKkIWg2GObwuJ6TCWB8qsL6q4',
                  '900293220-O76OTSxQzZeB7hvjlwujXYg7rDzN4Dy7bF4LBZn8', 'LGjLVWtiB8gloVC2nhi04KroTlJLtWiic803qiN296JFc')

tweedid=twitter.search(q='estonia',lang='en', count=100)
#variant1
twtekst=[]
for i in range(len(tweedid['statuses'])):
    twtekst.append(tweedid['statuses'][i]['text'])

raw=''.join(twtekst)    

twtekstlist=[]
for i in range(len(twtekst)):
    twtekstlist.append(twtekst[i])
len(twtekstlist)

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

#raw = raw.lower()
#tokens = tokenizer.tokenize(raw)
tokens=[]
for i in range(len(twtekstlist)):
    tokens.append(tokenizer.tokenize(twtekstlist[i]))
len(tokens)         

from stop_words import get_stop_words
# create English stop words list
en_stop = get_stop_words('en')
# remove stop words from tokens
#stopped_tokens = [i for i in tokens if not i in en_stop]
stopped_tokens=[]
for j in range(len(tokens)):
    stopped_tokens.append([i for i in tokens[j] if not i in en_stop])
len(stopped_tokens)

from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
#texts = [p_stemmer.stem(i) for i in stopped_tokens]
texts=[]
for j in range(len(stopped_tokens)):
    texts.append([p_stemmer.stem(i) for i in stopped_tokens[j]])

texts_clean=[]
myra=['co','t', 'http','o','rt', 'RT','https', '[0-9]']
puhas=[]
for j in range(len(texts)):
    puhas.append([i for i in tokens[j] if not i in myra])
print(puhas[0])
 
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
dictionary = Dictionary(puhas)
corpus = [dictionary.doc2bow(text) for text in puhas]

mudel = LdaModel(corpus=corpus, id2word=dictionary, iterations=50, num_topics=3)
 
import pyLDAvis.gensim
from gensim.models.coherencemodel import CoherenceModel
proov=pyLDAvis.gensim.prepare(mudel, corpus, dictionary) 
#save
pyLDAvis.save_html(proov, 'poov.html') 

teemad=mudel.print_topics(num_topics=3, num_words=3)
teemad

##teine variant mudelist
token_dict = {}

for i in range(len(twtekst)):
    token_dict[i] = twtekst[i]

from sklearn.feature_extraction.text import CountVectorizer
print("\n Build DTM")
%time tf = CountVectorizer(stop_words='english')

print("\n Fit DTM")
%time tfs1 = tf.fit_transform(token_dict.values())
  
# set the number of topics to look for
num = 5
import lda
model = lda.LDA(n_topics=num, n_iter=500, random_state=1)

# we fit the DTM not the TFIDF to LDA
print("\n Fit LDA to data set")
%time model.fit_transform(tfs1)

print("\n Obtain the words with high probabilities")
%time topic_word = model.topic_word_  # model.components_ also works

print("\n Obtain the feature names")
%time vocab = tf.get_feature_names()
  
topic_word = model.topic_word_

import matplotlib.pyplot as plt

# use matplotlib style sheet
try:
    plt.style.use('ggplot')
except:
    # version of matplotlib might not be recent
    pass  

%matplotlib inline
f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0,1,2,3,4]):
    ax[i].stem(topic_word[k,:], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-5,10)
    ax[i].set_ylim(0, 0.08)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("topic {}".format(k))

ax[4].set_xlabel("word")

plt.tight_layout()
plt.show()

doc_topic = model.doc_topic_
doc_topic.shape

#topic document
f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0, 5, 9, 14, 19]):
    ax[i].stem(doc_topic[k,:], linefmt='r-',
               markerfmt='ro', basefmt='w-')
    ax[i].set_xlim(-1, 5)
    ax[i].set_ylim(0, 1)
    #ax[i].set_axis_bgcolor('white')
    ax[i].set_axis_bgcolor((1,0.98,0.98))
    ax[i].set_ylabel("Prob")
    ax[i].set_title("Säuts {}".format(k))

ax[4].set_xlabel("Teema")

plt.tight_layout()
plt.show()



import numpy as np
import logging
import json
import warnings
warnings.filterwarnings('ignore')  # To ignore all warnings that arise here to enhance clarity



from numpy import array