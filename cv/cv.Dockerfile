FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip


RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install opencv-python-headless
RUN pip3 install numpy

WORKDIR /home/cv/src
CMD [ "python3", "camera.py" ]

ENV PORT=12345
EXPOSE 12345
