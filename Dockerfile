FROM python:slim-bookworm

WORKDIR /app

RUN apt update -y && apt install -y gcc

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]