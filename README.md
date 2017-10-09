# Species Finder

Species Finder is an app to find out who you really are based on a portrait.

# How to use this repository

With Docker installed and running, open up your Terminal and head over to the repository directory.

Type `docker build -t nameyouwanttogivetheimagehere .`, where you can replace nameyouwanttogivetheimagehere with a name you want to give the image. This will be the name/tag you can use instead of the ID of the image to run it.

Let it do its thing. Upon first running this, it will download a lot of things. This is a good thing.

Now type `docker run -it nameyouwanttogivetheimagehere /bin/bash` and then `python main.py portrait.jpg`
