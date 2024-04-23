FROM python:3.10

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY /app $APP_HOME/app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 8000
EXPOSE 8000

CMD exec uvicorn src.main:app --host 0.0.0.0 --port ${PORT} --workers 1