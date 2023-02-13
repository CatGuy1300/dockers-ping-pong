FROM ubuntu

RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev
RUN apt -yqq install python3.10-venv

WORKDIR /app
RUN python3 -m venv venv
COPY . .
RUN venv/bin/pip install -r requirements.txt

EXPOSE 5000
CMD [ "venv/bin/python", "pong.py" ]