# TextSimularityCalculator v0.1
TextSimularityCalculator will look at word embeddings and calculates the similarities between pieces of text.

# Problem
You need to find out whether two words are similar but not equal, for example when
you’re verifying user input and you don’t want to require the user to exactly enter the
expected word.

# Technologies

The main model we’ll use here is a version of Google’s Word2vec. This is not a deep
neural model. In fact, it is no more than a big lookup table from word to vector and
therefore hardly a model at all. The Word2vec embeddings are produced as a side
effect of training a network to predict a word from context for sentences taken from
Google News.

## Workflow

The program will download GoogleNews-vectors-negative300.bin using Keras and caches it under the src_root/generated folder.
Given the interested word it will check the binary file for similarities and returns the most similar words based on a sim score.

## Watch out!
The code will load the binary file in the memory - about 4G will be used!

