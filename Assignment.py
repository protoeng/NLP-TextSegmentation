
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import string
import nltk
import numpy as np
from nltk.stem.porter import *
from nltk.corpus import stopwords
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.metrics import windowdiff

# <codecell>

#Function to plot graphs required for Text Tiling Algorithm
def plot_fig(x,score,heading,fig_no):
    fig = plt.figure(fig_no,figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.plot(x,score,label=heading)
    ax.legend()

# <codecell>

#Open file in python
# -*- coding: utf-8 -*-
f = open('alien-life.txt','r')
doc=f.read()
f.close()
# The em-dash(long hyphen) is not recognised by ASCII. So, it is replaced with the hyphen.
if "—" in txt:
txt = txt.replace("—", "-")
#The original encoding of the text-file is in utf-8 format.So decoding the string from utf-8
doc=doc.decode('utf-8')
#Encoding it into ascii format
doc=doc.encode('ascii','ignore')
doc=doc.lower()

# <codecell>

#Saving a copy of original corpus along with the $$ sign to be later used for Windowdiff measure
doc_copy=doc
ref_word=[]
p = re.compile(r'(\n)|(\r)|(\t)|([!"#%&()*+,-./:;<=>?@\[\\\]^_`{|}~])', re.IGNORECASE)
doc_copy=re.sub(p,' ',doc_copy)
stemmer=PorterStemmer()
for word in doc_copy.split(" "):
    if word not in stopwords.words('english') and stemmer.stem_word(word) not in stopwords.words('english'):
        if word!=" " and word!="":
            ref_word.append(stemmer.stem_word(word))

# <headingcell level=3>

# TextTiling Algorithm

# <codecell>

#Preparation for TextTiling Algorithm Implementation
#Stripping punctuation
#Removing new-line characters and punctuations
p = re.compile(r'(\n)|(\r)|(\t)|([!"#$%&()*+,-./:;<=>?@\[\\\]^_`{|}~])', re.IGNORECASE)
doc=re.sub(p,' ',doc)

# <codecell>

#Sen_length represents the desired sentence length that we are focusing on 
#Doc represents the corpus of text
#Fig no represents the figure no that we want to give to the graph
def text_tiling(doc,sen_len,fig_no):
    
    #Porter Stemming and removing stop words
    stemmer=PorterStemmer() 
    sentences=[]
    sentence=""
    j=0
    for word in doc.split(" "):
        if word not in stopwords.words('english') and word!=" " and word!="":
            j=j+1
            sentence=sentence + stemmer.stem_word(word)+' '
            if j==sen_len:
                # -1 is to prevent the whitespace that is appended at the end to be included in the sentence
                sentences.append(sentence[:-1])
                sentence=""
                j=0
    #If the last sentence is of length less than sen_length
    sentences.append(sentence[:-1])
 
    #Vectorizing Sentences using Sklearn to determine Cosine Similarity between adjacent sentences
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    score=[]
    for i in range(0,tfidf_matrix.shape[0]-2):
        score.append(cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix[i+1:i+2])[0][0])
    
    #Plotting Cosine Similarity 