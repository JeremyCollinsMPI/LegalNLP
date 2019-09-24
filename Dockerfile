FROM jeremycollinsmpi/bert-as-service
RUN pip install python-docx bert-serving-client bert-serving-server pymongo
RUN apt-get update
RUN apt-get install -y mongodb-clients