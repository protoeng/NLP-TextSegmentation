
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
