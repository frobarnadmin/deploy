# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Start Django app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]