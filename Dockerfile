#FROM joyzoursky/python-chromedriver
#FROM deinchristian/rpi-selenium-base:latest
#FROM deinchristian/rpi-selenium-node-chrome
#FROM ubuntu:18.04
FROM arm32v7/python:3-alpine

# update apk repo
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# upgrade pip
RUN pip install --upgrade pip

# install selenium
#RUN pip install selenium

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

#ENTRYPOINT /bin/sh
