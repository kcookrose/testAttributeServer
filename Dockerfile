FROM tensorflow/tensorflow

RUN apt-get update && apt-get install -y --no-install-recommends \
	curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python-numpy \
        python-pip \
        python-scipy \
        git \
        libhdf5-dev \
        graphviz \
        && \
    	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN pip install keras

RUN apt-get install python3 

COPY keras.json /root/.keras/keras.json

ADD . /app

WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]



