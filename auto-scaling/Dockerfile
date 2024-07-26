FROM python:3.9.5

WORKDIR /app

COPY main.py /app

RUN pip install fastapi uvicorn[standard]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
