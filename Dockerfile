FROM ubuntu:18.04
RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN echo 'alias python="python3.6"' >> ~/.bashrc

RUN pip install --upgrade pip
RUN pip install -U python-docx pymongo virtualenv textrazor
RUN apt-get install -y mongodb-clients
RUN pip install flask flask_restful wtforms
RUN apt-get install -y wget jq
RUN pip install requests
RUN pip install numpy
RUN pip install html2text
RUN pip install sklearn
RUN pip install nltk
WORKDIR /directory
#RUN virtualenv /keras
#RUN /keras/bin/pip install tensorflow==2.0.0-rc0 sklearn pandas 
