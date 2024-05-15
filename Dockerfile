# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code/

COPY pyproject.toml /code/

# install dependencies
RUN pip install -e .

COPY ./main.py /code/

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "80"]
