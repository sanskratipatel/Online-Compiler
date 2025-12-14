FROM python:3.12-slim

WORKDIR /code

# Prevent interactive input
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
