##############################################################################
# Script Name: Dockerfile
# Author: CSA
# Description: run exl_my_app in docker container
# Company:     Exlibris
##############################################################################

FROM poc-nexus01.dc99:8123/exl_python_builder:latest

ENV EXL_ENV ${EXL_ENV}
ENV VAULT_TOKEN ${VAULT_TOKEN}

RUN mkdir /src
ADD requirements.txt /src/requirements.txt

WORKDIR /src

# print even more verbose debug logs (console only) 1 - enabled 0 (or any) - disabled
ENV EXL_TRACE 1

RUN pip install -r requirements.txt --upgrade

ADD . /src

ENTRYPOINT [ "python" , "exl_main.py" ]
