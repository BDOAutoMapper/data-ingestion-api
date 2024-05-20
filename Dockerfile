# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code/

COPY pyproject.toml /code/

# install dependencies
RUN pip install -e .

COPY ./main.py /code/

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "80"]

# build image with: docker build -t fastapi-demo .
# run with: docker run -dp 127.0.0.1:80:80 fastapi-demo
