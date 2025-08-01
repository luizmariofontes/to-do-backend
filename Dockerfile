FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["/bin/bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

