FROM ubuntu:yakkety

RUN groupadd -r hc && useradd -r -m -g hc hc

# Install deps
RUN set -x && apt-get -qq update \
    && apt-get install -y \
        python3-setuptools \
        python3-pip \
        python3-psycopg2 \
        python3-rcssmin \
        python3-rjsmin \
        python3-mysqldb \
        subversion \
        uwsgi \
        uwsgi-plugin-python3 \
        --no-install-recommends \
    && svn export https://github.com/healthchecks/healthchecks/tags/v1.0.1 /app \
    && pip3 install --no-cache-dir -r /app/requirements.txt \
    && pip3 install --no-cache-dir braintree raven \
    && apt-get clean \
    && rm -fr /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN python3 manage.py collectstatic --noinput && python3 manage.py compress

USER hc

EXPOSE 5000

CMD [ "/usr/bin/uwsgi-core", "uwsgi.ini" ]
