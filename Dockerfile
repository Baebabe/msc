FROM python:3.12.4-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y curl wget

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory to /app/
COPY . /app/

# Create static directory if it doesn't exist
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/static

# Ensure static files directory exists
RUN if [ ! -d /app/static/admin ]; then mkdir -p /app/static/admin; fi

# Copy admin static files
RUN python -c "import django; from django.contrib import admin; print(admin.__path__[0])" | xargs -I {} cp -r {}/static/admin /app/static/

# Collect static files
RUN python manage.py collectstatic --noinput --clear

COPY start-server.sh /app/

# Ensure the start-server script is executable
RUN chmod +x /app/start-server.sh

# Verify the contents of the /app directory
RUN ls -l /app/

# Expose port 7188 for the application
EXPOSE 7188

# Run the application using gunicorn instead of runserver for production
CMD ["gunicorn", "mscteachers.wsgi:application", "--bind", "0.0.0.0:7188"]