FROM jeremycollinsmpi/bert-as-service
RUN pip install -U python-docx pymongo bert-serving-client bert-serving-server 
RUN apt-get update
RUN apt-get install -y mongodb-clients