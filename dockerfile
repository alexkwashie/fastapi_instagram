FROM python:3.10

WORKDIR /fastapi_instagram

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

ENV PYTHONPATH=/fastapi_instagram
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
