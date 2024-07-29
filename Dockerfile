FROM python:3.10-alpine

WORKDIR /app

RUN pip install requests

COPY load_models.py /app/load_models.py

CMD ["python", "/app/load_models.py"]