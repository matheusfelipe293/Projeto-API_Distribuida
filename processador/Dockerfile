FROM python:3.13-slim
WORKDIR /app
COPY main.py .
RUN pip install fastapi uvicorn httpx
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]