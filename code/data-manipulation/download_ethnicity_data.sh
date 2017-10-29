#!/usr/bin/env bash

wget http://wiki.cnbc.cmu.edu/images/asian.zip
wget http://wiki.cnbc.cmu.edu/images/africanamerican.zip
wget http://wiki.cnbc.cmu.edu/images/caucasian.zip
wget http://wiki.cnbc.cmu.edu/images/hispanic.zip
wget http://wiki.cnbc.cmu.edu/images/multiracial.zip

unzip asian.zip -d asian
unzip africanamerican.zip -d africanamerican
unzip caucasian.zip -d caucasian
unzip hispanic.zip -d hispanic
unzip multiracial.zip -d multiracial

mkdir ethnicity

cp -r asian/Asian ethnicity/
cp -r africanamerican/Black ethnicity/
cp -r caucasian/Caucasian ethnicity/
cp -r hispanic/Hispanic ethnicity/
cp -r multiracial/Multiracial ethnicity/

rm -r asian
rm -r africanamerican
rm -r caucasian
rm -r hispanic
rm -r multiracial

rm asian.zip
rm africanamerican.zip
rm caucasian.zip
rm hispanic.zip
rm multiracial.zip

mv ethnicity/ ../../datasets/
