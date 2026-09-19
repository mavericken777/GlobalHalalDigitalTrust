FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY policies ./policies
ENV PYTHONPATH=/app/src
EXPOSE 8080
CMD ["uvicorn", "ahte.api:app", "--host", "0.0.0.0", "--port", "8080"]
