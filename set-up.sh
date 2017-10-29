#!/usr/bin/env bash

pyhon3 -m venv --system-site-packages env

source env/bin/activate

pip install -r requirements.txt
pip install h5py