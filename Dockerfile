FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "personal_assistant/main.py"]