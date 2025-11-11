# app/modules/users/migrations/env.py
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# This must match your alembic.ini path
config = context.config
fileConfig(config.config_file_name)
target_metadata = None  # Not using ORM models

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"), poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(connection=connection)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
