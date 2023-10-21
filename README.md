This project evaluates a text document named ‘alien-life.txt’, aiming to identify all potential segment boundaries using the TextTiling algorithm. The segment boundaries are indicated with “$$” within the text. The project involves the following tasks:

1. Removal of all punctuation and converting all characters to lower case.
2. Function words are eliminated (link to the function words list is provided).
3. Stemming is carried out (NLTK can be used for this step).
4. The TextTiling algorithm is implemented without the use of the NLTK library to segment the 'alien-life.txt' file. We use the (m-sigma) as the threshold where m is the average depth score and sigma is the standard deviation.
5. The Windowdiff measure is implemented and the segmentation performance reported.
6. The pseudo sentence length is varied from 10 to 100 and the Windowdiff value is plotted to ascertain the optimal pseudo sentence length.

Note: Although any programming language may be utilized for the implementation, th