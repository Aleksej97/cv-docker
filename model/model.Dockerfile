FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install numpy
RUN pip3 install tensorflow

WORKDIR /home/model/src
CMD [ "python3", "model.py" ]

ENV PORT=8080
EXPOSE 8080
