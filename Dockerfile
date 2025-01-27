FROM python:3.12

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Command to run the application
CMD gunicorn mscteachers.wsgi:application --bind 0.0.0.0:7188