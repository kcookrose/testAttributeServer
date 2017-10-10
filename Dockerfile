FROM tensorflow/tensorflow

RUN pip install --upgrade pip && \
    pip install --upgrade tensorflow && \
    pip install --upgrade matplotlib && \
    pip install --upgrade numpy && \
    pip install requests pip && \
    pip install keras

RUN apt-get install python3

COPY keras.json /root/.keras/keras.json

ADD . /species-finder

WORKDIR "/species-finder/notebooks"