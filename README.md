# LegalNLP
This project is for fuzzy search of terms in a directory.

#How to run it
Install docker.  In the directory, run:

bash run.sh
This starts three docker images: an image for Stanford CoreNLP; an image for MongoDB; and the docker image for this project.
The script starts the docker container.  To run the api, run

python api.py

# Loading documents
To analyse documents, place them in the folder Files.  In the api, then go to
http://0.0.0.0:5000/load
This will analyse the documents and load the segmented sentences into MongoDB.

# Searching
1. Searching for words
Single word search is done in http://0.0.0.0:5000/search.
Multiple word search is done in http://0.0.0.0:5000/multiple.  To use this, type words which should be in the sentence separated by a space (e.g. 'London Paris' to return sentences containing both 'London' and 'Paris').

2. Searching for hyponyms using wordnet
Go to http://0.0.0.0:5000/search_hyponym.  This returns sentences containing hyponyms of the search word.

3. Searching for hyponyms using conceptnet
For this, conceptnet data has to be loaded into mongo.  This can be done by running

python conceptnet.py

The api for searching for hyponyms using conceptnet is http://0.0.0.0:5000/conceptnet


