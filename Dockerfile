FROM python:alpine

RUN pip install nltk
WORKDIR /app

COPY . /app/

CMD ["python", "words_counter.py"]