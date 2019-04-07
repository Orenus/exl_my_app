FROM exl_python_builder:latest

ENV EXL_ENV ${EXL_ENV}
ENV VAULT_TOKEN ${VAULT_TOKEN}

RUN mkdir /src
ADD requirements.txt /src/requirements.txt

# print even more verbose debug logs (console only) 1 - enabled 0 (or any) - disabled
ENV EXL_TRACE 1

RUN pip install -r /src/requirements.txt --upgrade

ADD . /src

ENTRYPOINT [ "python" , "/src/exl_my_app.py" ]
