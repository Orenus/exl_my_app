FROM exl_python_builder:latest

RUN mkdir /src
ADD requirements.txt /src/requirements.txt

WORKDIR /src

# print even more verbose debug logs (console only) 1 - enabled 0 (or any) - disabled
ENV EXL_TRACE 1

RUN pip install -r requirements.txt --upgrade

ADD ./config/global.properties /etc/
ADD . /src