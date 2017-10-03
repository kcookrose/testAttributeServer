# Species Finder

Species Finder is an app to find out who you really are based on a portrait.

# How to use this repository

With Docker installed and running, open up your Terminal and head over to the repository directory.

Type `docker build -t nameyouwanttogivtheimagehere .`, where you can replace nameyouwanttogivtheimagehere with a name you want to give the image. This will be the name/tag you can use instead of the ID of the image to run it.

Let it do its thing. Upon first running this, it will download a lot of things. This is a good thing.

Now type `docker run nameyouwanttogivtheimagehere` where nameyouwanttogivtheimagehere is the name you gave the image during the previous step. (Yes, this could be nameyouwanttogivtheimagehere.)

What should happen is that app.py is run inside the image, which has a fully functioning TensorFlow/Keras enviornment installed. app.py contains the example code from the Keras repository for training a Neural Net on the MNISt dataset to classify handwritten digits. Classic.

# Acknoledgements

Test portrait: https://unsplash.com/photos/das6NrjLoM0
