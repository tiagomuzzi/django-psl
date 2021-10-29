# Django + PostgresSQL + Docker

This exercise is to containerize a simple Django/Postgresql application using Docker.

## Pre-requisites

* Docker (compatible with 20.10)

* Poetry >= 1.1.11

## Instructions

1. Fork the repo and do a git clone 
  
  git clone https://github.com/tiagomuzzi/django-psl.git
  
2. If you have docker installed:
```
docker-compose up --build -d   # Run the container.

docker-compose down   # Stop and remove everything.

```

The site will be available to you at `localhost:8000`.

