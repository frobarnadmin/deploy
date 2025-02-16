# Django Hello World App Deployment Guide

## 1. Creating a Simple Hello World Django App

This section covers setting up a simple Django application that returns "Hello, World!".

### 1.1 Install Django
Ensure Python is installed, then install Django:
```bash
pip install django
```

### 1.2 Create a Django Project
Run the following command:
```bash
django-admin startproject myapp
cd myapp
```

### 1.3 Create a Django App
```bash
python manage.py startapp hello
```

### 1.4 Modify `views.py`
Edit `hello/views.py` to return "Hello, World!":
```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

### 1.5 Update `urls.py`
Edit `myapp/urls.py` to map the view:
```python
from django.contrib import admin
from django.urls import path
from hello.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name='hello-world'),
]
```

### 1.6 Run the Server
Start the server and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/):
```bash
python manage.py runserver
```

---

## 2. Setting Up GitHub Actions Workflow

GitHub Actions automates testing and deployment.

### 2.1 Create GitHub Actions Workflow File
Create `.github/workflows/main.yml` and add the following:
```yaml
name: Django CI/CD

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          python manage.py test
```

---

## 3. Building and Pushing Docker Image to Docker Hub

### 3.1 Create a `Dockerfile`
```dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install django gunicorn

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
```

### 3.2 Build and Push Docker Image
```bash
docker build -t myapp .
docker tag myapp <dockerhub-username>/myapp:latest
docker login
docker push <dockerhub-username>/myapp:latest
```

---

## 4. Deploying to Kubernetes on DigitalOcean

### 4.1 Create Kubernetes Deployment File
Create `k8s/deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: django
  template:
    metadata:
      labels:
        app: django
    spec:
      containers:
      - name: django
        image: <dockerhub-username>/myapp:latest
        ports:
        - containerPort: 8000
```

### 4.2 Create Kubernetes Service File
Create `k8s/service.yaml`:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: django-service
spec:
  selector:
    app: django
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: LoadBalancer
```

### 4.3 Apply Kubernetes Configurations
Run the following commands:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc django-service
```

### 4.4 Verify Deployment
Ensure the app is running:
```bash
kubectl get pods
kubectl get services
```

---

## 🎯 Summary
This guide covered:
- Creating a **Django Hello World** application
- Setting up **GitHub Actions for CI/CD**
- Dockerizing and pushing to **Docker Hub**
- Deploying to **Kubernetes on DigitalOcean**
