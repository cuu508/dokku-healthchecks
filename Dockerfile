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
    && svn export https://github.com/healthchecks/healthchecks/trunk /src \
    && pip3 install --no-cache-dir -r /src/requirements.txt \
    && pip3 install --no-cache-dir braintree \
    && apt-get clean \
    && rm -fr /var/lib/apt/lists/*

WORKDIR /src

COPY local_settings.py /src/hc
COPY uwsgi.ini /src/uwsgi.ini

RUN touch /src/hc.sqlite && chown hc:hc /src/hc.sqlite
RUN python3 manage.py collectstatic --noinput && python3 manage.py compress

EXPOSE 9090

CMD [ "uwsgi", "uwsgi.ini" ]
