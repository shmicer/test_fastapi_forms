FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN python3 -m pip install -r requirements.txt

WORKDIR /src

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]