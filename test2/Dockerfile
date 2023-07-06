FROM python:3.11-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry
RUN pip install python-jose[cryptography]
RUN pip install passlib[bcrypt]

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT ["poetry", "run","uvicorn", "api.main:app", "--host", "0.0.0.0","--reload"]
