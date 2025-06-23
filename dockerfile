FROM python:3.10

WORKDIR /fastapi_instagram

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./instagram ./instagram

ENV PYTHONPATH=/fastapi_instagram
CMD ["uvicorn", "instagram.main:app", "--host", "0.0.0.0", "--port", "80"]
