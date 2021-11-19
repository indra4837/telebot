FROM python:3.8-slim
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY *.txt .
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt
COPY . ./

# Expose port 3000
EXPOSE 3000
ENV PORT 3000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
