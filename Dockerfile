FROM python:3.7-alpine

WORKDIR /app
COPY . /app

RUN apk update && apk add linux-headers

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python","coast.py"]