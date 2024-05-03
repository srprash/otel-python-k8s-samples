FROM python:3.11

WORKDIR /app

COPY . ./

RUN rm -rf venv

RUN pip install -r requirements.txt

ENV LISTEN_ADDRESS=0.0.0.0:8080

EXPOSE 8080

# CMD ["python", "app.py"]

CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]