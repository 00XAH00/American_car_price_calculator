FROM python:3.11
RUN mkdir /app
COPY . /app
COPY pyproject.toml /app
EXPOSE 5873

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["poetry", "run", "python", "main.py"]
