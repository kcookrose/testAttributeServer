# Species Finder

Species Finder is an app to find out who you really are based on a portrait.

# How to use this repository

## Basics

If you have a python installation named `python3` you can do the following:

When you pull this repository for the first time and want to get started, change to the repo directory in a terminal and type:

`./set-up.sh`

This should install the basic requirements for you and source the virtual environment so you are ready to go.

If your python installation isn't called `python3` (but `python` for example) you still need to do this by hand:

`python -m venv env`
`source env/bin/activate (linux based) or call env/Scripts/activate (Windows)`
`pip install -r requirements.txt`
`pip install h5py`

What you want to do after this depends on what you are here to do.

## Just run the Command Line App

If you want to classify an image using our industry strength image recognition technology you have to type the following:

`python code/app/main.py code/app/portrait.jpg`

This should print two things in the end: asian and male. This tells you that our classifier thinks that our sample image of a hat-wearing male heartlander is indeed a picture of a male ... asian person. (We haven't had the chance to finetune our model yet. But it's already at 72.5% accuracy - which isn't too bad, really.)

If you want to see what our app thinks of your image, simply replace the `code/app/portrait.jpg` in the call with the path to your image. Again, our classifiers aren't finetuned yet.

## Train a Classifier on Gender Data

Still in the repo's root folder run:

`./code/data-manipulation/download_wiki_data.sh`

This then loads and extracts the wiki dataset from https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/ and should put it in a (maybe newly created) `datasets` folder in the repo's root.

Now run:

`python code/data-manipulation/arrange_wiki_data.py gender 100 40 -c`

This cleans up the base wiki dataset and moves the specified amount of training images (100) and validation images (40) for each class into a new gender-data folder inside the datasets folder.

You can now run:

`python code/classifiers/gender-transfer/multiclass.py`

 ... which should start the learning process.

## Train a Classifier on Ethnicity Data

Still in the repo's root folder run:

`./code/data-manipulation/download_ethnicity_data.sh`

This then loads and extracts the ethnicity dataset from http://wiki.cnbc.cmu.edu/ and should put it in a (maybe newly created) `datasets` folder in the repo's root.

Now run:

`python code/data-manipulation/arrange_ethnicity_data.py 100 40`

This moves 100 training images and 40 validation images per class into a folder named ethnicity-data inside the datasets folder.

You can now run:

`python code/classifiers/ethnicity-transfer/multiclass.py`

 ... which should start the learning process.

## Have a Look at the Notebooks

To run the Jupyter notebook server run:

`cd code/notebooks`

`jupyter notebook`

## Run the Server

Install flask, go into the code/app folder and run:

Linux: `FLASK_APP=server.py flask run`

Windows: `set FLASK_APP=server.py` then `flask run` (may require pip install pillow)

You can then upload images to the server from any html with this form:

`<form action="http://127.0.0.1:5000/classification/portrait" enctype=multipart/form-data method="POST">
		<input type="file" name="file">
		<input type="submit" name="">
	</form>`
 
You'll get back a JSON Response that looks similar to this:
 
`{
 ethnicity:	"Asian"
 gender:	"male"
}`

# Acknowledgment

Test portrait: https://unsplash.com/photos/das6NrjLoM0
