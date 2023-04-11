FROM --platform=linux/amd64 python:3.10-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

ARG CONFIG=local
ENV CONFIG ${CONFIG}
COPY . .

ENTRYPOINT [ "python", "-u" ]
