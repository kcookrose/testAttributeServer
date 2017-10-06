FROM floydhub/dl-docker:cpu

COPY keras.json /root/.keras/keras.json

ADD . /app

WORKDIR /app