
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