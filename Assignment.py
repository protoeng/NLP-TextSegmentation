
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
