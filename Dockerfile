FROM python:3.12.2-slim

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src/app

EXPOSE 5000

CMD ["python", "main.py"]