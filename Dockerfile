FROM python:3.12.0b2-alpine3.17
WORKDIR /enigma
RUN apk update
COPY . .
EXPOSE 8080
CMD ["python", "/enigma/app.py"]

