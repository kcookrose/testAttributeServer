# Species Finder

Species Finder is an app to find out who you really are based on a portrait.

# How to use this repository

With Docker installed and running, open up your Terminal and head over to the repository directory.

Type `docker build -t nameyouwanttogivetheimagehere .`, where you can replace nameyouwanttogivetheimagehere with a name you want to give the image. This will be the name/tag you can use instead of the ID of the image to run it.

Let it do its thing. Upon first running this, it will download a lot of things. This is a good thing.

Now run this, but only once:

`docker run -it -p 8888:8888 -p 6006:6006 -v /$(pwd)/notebooks:/notebooks --name notebooks nameyouwanttogivetheimagehere`

The notebook server should spin up and the terminal should tell you something like the following:

`Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=LONGTOKENDISPLAYEDHERE`

Do that, and if you want to shut this down, just hit ctrl+c twice.

If you want to spin this container up in the future, use `docker start -i tf`

NOTES:

* Sadly, I couldn't test this on Windows, but according to [this SO thread](https://stackoverflow.com/questions/33636925/how-do-i-start-tensorflow-docker-jupyter-notebook) you'll have to do some port forwarding. As far as I know, Docker on Windows no longer uses VirtualBox, so you'll have to input the rules shown on the screenshot in the first answer into the Docker settings for ports.

* Any changes you make to the /notebooks directory should, in theory, be persisted across sessions and changes you make to it on you Windows host should be visible inside the Docker image/Jupyter Web Interface. Get back to me with info if this is indeed working. If it is, you can simply put stuff like data sets etc. in here and experiment with notebooks.

