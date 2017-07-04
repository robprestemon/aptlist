FROM python:3.6.1-alpine

RUN apk add --no-cache gcc musl-dev linux-headers postgresql-dev

ADD . /code
WORKDIR /code
ENV PYTHONPATH $PYTHONPATH:/code
RUN pip3.6 install -r requirements.txt
CMD ["python3.6", "/code/main.py"]