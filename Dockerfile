FROM python:3.11.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["src/docker/app.sh"]
