FROM exl-python-builder:latest

RUN mkdir /src
ADD . /src

WORKDIR /src
# host name of artifacts server
ARG ARTIFACTORY_HOST
# print even more verbose debug logs (console only) 1 - enabled 0 (or any) - disabled
ENV EXL_TRACE 1

RUN pip install -r requirements.txt --upgrade --trusted-host ${ARTIFACTORY_HOST}

ADD ./config/global.properties /etc/