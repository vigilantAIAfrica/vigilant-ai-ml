FROM python:3.10-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY . .
# This assumes you have a main.py; if not, we'll create one next
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
