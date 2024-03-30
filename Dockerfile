FROM python:3.12.2

WORKDIR /code/data

COPY /data/test.csv /data/train.csv /code/data/

WORKDIR /code

COPY train.py test.py requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

RUN python train.py

CMD ["python", "test.py"]
