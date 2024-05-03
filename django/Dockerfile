FROM python:3.11

WORKDIR /app

# Install dependencies
COPY djangoApp/requirements.txt /app/

RUN pip install -r requirements.txt

# when using command line instrumentation
# RUN pip install opentelemetry-distro opentelemetry-exporter-otlp
# RUN opentelemetry-bootstrap -a install

# Copy the project code into the container
COPY djangoApp/. /app/

EXPOSE 8000

# when using command line instrumentation
# ENV DJANGO_SETTINGS_MODULE=djangoApp.settings
# CMD ["opentelemetry-instrument", "python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

# when using k8s operator for instrumentation
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

# when using gunicorn
# CMD ["gunicorn", "djangoApp.wsgi:application", "--bind", "0.0.0.0:8000"]