FROM python:3.8-alpine
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask
COPY . . 
EXPOSE 5000
CMD ["python3", "app.py"]
