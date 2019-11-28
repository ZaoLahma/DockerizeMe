FROM python:3

WORKDIR /app
COPY ./services/docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main_services.py" ]
