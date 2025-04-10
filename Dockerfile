FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y nano \
    && pip install flask 
    
EXPOSE 3000

CMD ["python", "app.py"]