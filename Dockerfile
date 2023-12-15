FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
EXPOSE 9730

ENV NOM GODWIN

CMD [ "python", "main.py" ]