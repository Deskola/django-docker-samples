# Pull base image
FROM python:3.10.4-slim-bullseye

# Set env variables
ENV PIP_DISABLED_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependecies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy projetc
COPY . .
