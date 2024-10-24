FROM python:3.9-slim

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1  
# Ensures that Python output is sent straight to terminal without buffering

WORKDIR /app

# Copy the requirements file first for better caching of layers
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Use Gunicorn as the WSGI server to serve the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
