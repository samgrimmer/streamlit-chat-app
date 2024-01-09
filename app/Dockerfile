FROM python:3.9-slim

COPY requirements.txt requirements.txt

RUN pip install -U pip

RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8501

# Run
ENTRYPOINT streamlit run main.py --server.port=8501 --server.address=0.0.0.0