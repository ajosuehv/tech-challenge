FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev libpq-dev && \
    # Dependency manager for python
    pip install --no-cache-dir -r requirements.txt &&\
    apt-get autoremove -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -r container && useradd -r -g container container
RUN chown container:container -R /usr/src/app


COPY . .
RUN chmod 755 /usr/src/app

USER container


HEALTHCHECK --interval=10s --timeout=2s --start-period=15s \
    CMD wget --quiet --tries=1 --spider http://localhost:5000/health-check || exit 1

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--reload", "app:app", "–w", "2", "--threads", "3", "-t", "240"]
