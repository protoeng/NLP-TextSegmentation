This project evaluates a text document named ‘alien-life.txt’, aiming to identify all potential segment boundaries using the TextTiling algorithm. The segment boundaries are indicated with “$$” within the text. The project involves the following tasks:

1. Removal of all punctuation and converting all characters to lower case.
2. Function words are eliminated (link to the function words list is provided).
3. Stemming is carried out (NLTK can be used for this step).
4. The TextTiling algorithm is implemented without the use of the NLTK library to segment the 'alien-life.txt' file. We use the (m-sigma) as the threshold where m is the average depth sco