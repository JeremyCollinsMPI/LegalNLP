FROM jeremycollinsmpi/bert-as-service
RUN pip install --upgrade pip
RUN pip install -U python-docx pymongo bert-serving-client bert-serving-server tensorflow==2.0.0-rc0 sklearn pandas
RUN apt-get update
RUN apt-get install -y mongodb-clients