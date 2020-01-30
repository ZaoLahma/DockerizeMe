FROM python:3

VOLUME ["/app/file_storage/files"]

WORKDIR /app
COPY ./file_storage/docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main_file_storage.py" ]
