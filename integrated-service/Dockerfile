FROM python:3.9.5

WORKDIR /app

RUN pip install motor fastapi uvicorn[standard]

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]