import peewee_async
from settings.base import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
)

DATABASE = peewee_async.PooledPostgresqlDatabase(
    user=POSTGRES_USER,
    host=POSTGRES_HOST,
    database=POSTGRES_DB,
    password=POSTGRES_PASSWORD,
)