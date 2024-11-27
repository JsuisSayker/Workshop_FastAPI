FROM python:alpine3.20 as fastapi

WORKDIR /app

RUN python -m venv .venv
RUN source .venv/bin/activate

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . ./
COPY ./.env /app/.env
COPY ./run_migration.sh /app/run_migration.sh
COPY ./alembic.ini /app/alembic.ini

CMD ["/app/run_migration.sh"]