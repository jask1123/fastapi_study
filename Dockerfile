FROM python:3.11-buster

ENV PYTHONUNBUFFRED=1

WORKDIR /src

RUN pip install poetry

COPY pyroject.tole* poetry.lock* ./

RUN poetry config virtualenvs.create true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT ["poetry", "run","uvicorn", "api.main:app", "--host", "0.0.0.0","--reload"]