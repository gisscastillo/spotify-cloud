FROM python:3.9-slim
WORKDIR /helper
RUN pip install flask
COPY . .
CMD ["python", "status.py"]