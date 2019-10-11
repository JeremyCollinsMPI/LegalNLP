FROM tensorflow/tensorflow:1.12.0-py3
RUN pip install --upgrade pip
RUN pip install -U python-docx pymongo virtualenv textrazor
RUN apt-get update
RUN apt-get install -y mongodb-clients
RUN pip install flask flask_restful wtforms
#RUN virtualenv /keras
#RUN /keras/bin/pip install tensorflow==2.0.0-rc0 sklearn pandas
WORKDIR /directory