ARG IMAGE_VERSION=3.7

FROM python:$IMAGE_VERSION

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "/app/app.py" ]
