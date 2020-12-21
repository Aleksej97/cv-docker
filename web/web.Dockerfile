FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install flask
RUN pip3 install requests

WORKDIR /home/web/src
CMD [ "python3", "main.py" ]

ENV PORT=5000
EXPOSE 5000

