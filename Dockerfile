FROM python:3.10-alpine
WORKDIR /opt/app/src

# Install the application dependencies
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY ./ ./
EXPOSE 8000

# Setup an app user so the container doesn't run as the root user
RUN adduser app --disabled-password
USER app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]