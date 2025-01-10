FROM alpine:3.14
FROM python:3.12.8-alpine3.21
WORKDIR /opt/app/

# Install the application dependencies
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY ./ ./src
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN adduser app --disabled-password
USER app

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]