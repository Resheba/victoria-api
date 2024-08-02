FROM python:3.11.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code

COPY . .

EXPOSE 80

CMD ["docker/app.sh"]
