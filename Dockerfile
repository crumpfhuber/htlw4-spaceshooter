FROM python:3

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt --no-index

CMD [ "python", "./main.py" ]
