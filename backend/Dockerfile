# Dockerfile
# Use a lightweight official Python runtime base image
FROM python:3.11-slim

# Copy the app.py file into the container
COPY app.py .

# Expose the port your server listens on
EXPOSE 8080

# Run the HTTP server when the container starts
CMD ["python", "app.py"]