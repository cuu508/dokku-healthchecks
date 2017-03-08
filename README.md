Healthchecks on Dokku
=====================

Docker image to run the [healthchecks](https://github.com/healthchecks/healthchecks)
django application on Dokku

*N.B.* Due to no tagging on the healthchecks repository this will always build with the latest commit

## Building

```
docker build -t cuu508/healthchecks .
```

## Running

```
docker run -p 5000:5000 cuu508/healthchecks
```

The container is now accepting requests on port 5000.

## Admin Access

By default no admin user is created. To create your first admin user connect to your running docker container and run:

```
./manage.py createsuperuser
```

You will now be able to login to the admin at http://localhost:9090/admin.

*N.B.* There is no validation so ensure you correctly set an email address and password or you may find yourself unable to login.

## Configuration

This image is built to take basic configuration from environment variables passed:

```
docker run -p 5000:5000 \
           -e HC_DEBUG=False \
           -e HC_HOST=example.org \
           -e HC_SITE_ROOT="http://localhost:9090" \
           -e HC_DB=postgres \
           -e HC_DB_HOST=localhost \
           -e HC_DB_PORT=5432 \
           -e HC_DB_USER=root \
           -e HC_DB_PASSWORD=pa55word\
           -e HC_EMAIL_FROM="healthchecks@example.org" \
           -e HC_EMAIL_HOST=localhost \
           -e HC_EMAIL_PORT=25 \
           -e HC_EMAIL_USER="" \
           -e HC_EMAIL_PASSWORD="" \
          cuu508/healthchecks
```
