FROM jeremycollinsmpi/bert-as-service
RUN pip install --upgrade pip
RUN pip install -U python-docx pymongo bert-serving-client bert-serving-server virtualenv
RUN apt-get update
RUN apt-get install -y mongodb-clients
RUN virtualenv /keras
RUN /keras/bin/pip install tensorflow==2.0.0-rc0 sklearn pandas