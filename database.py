import os
import psycopg2
import urlparse


urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["elmer.db.elephantsql.com"])

conn = psycopg2.connect(database =url1.path[1:]
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
)
