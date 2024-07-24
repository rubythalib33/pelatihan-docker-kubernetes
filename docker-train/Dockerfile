FROM python:3.9.5

WORKDIR /app

ENV HOST='0.0.0.0'

RUN pip install fastapi uvicorn[standard]

COPY app.py app.py

CMD ["python", "app.py"]