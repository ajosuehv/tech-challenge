FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev libpq-dev && \
    apt-get autoremove -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
RUN groupadd -r container && useradd -r -g container container
RUN chown container:container -R /usr/src/app


COPY main.py .
COPY api ./api/
RUN chmod 755 /usr/src/app

USER container

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--reload", "main:app", "–w", "2", "--threads", "3", "-t", "240"]
