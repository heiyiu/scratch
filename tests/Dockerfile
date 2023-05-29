FROM python:3.11-slim

COPY ./requirements.txt ./test_deploy.py /app/
RUN pip install -r /app/requirements.txt

CMD ["pytest", "/app/"]