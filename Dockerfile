FROM ubuntu:22.04

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.10 python3-distutils python3-pip python3-apt

RUN python3 -m pip install --no-cache-dir -r $APP_HOME/requirements.txt

## Build phase
RUN python3 $APP_HOME/train.py

EXPOSE 80

CMD ["python3", "${APP_HOME}/test.py"]

