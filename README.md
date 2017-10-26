# Species Finder

Species Finder is an app to find out who you really are based on a portrait.

# How to use this repository

## A Bit of Python History

Okay, since Docker's the worst, we'll use venv instead. What's venv you ask? Well ... let's start at the beginning.

There once was a tool called virtualenv:

"virtualenv solves a very specific problem: it allows multiple Python projects that have different (and often conflicting) requirements, to coexist on the same computer." [SOURCE](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)

virtualenv was the standard for creating virtual python enviroments up until python version 3.3. That's when the python developers created their own, native implementation of the concept. Here's another quote:

"If you are using Python 3 then you should already have pyvenv installed. This is a file that uses the venv library underneath.

From here on out we’ll assume you’re using the newer pyvenv tool, since there are few differences between it and virtualenv with regard to the actual commands. In reality, though, they are very different tools." [SOURCE](https://realpython.com/blog/python/python-virtual-environments-a-primer/)

So venv was their library that was then wrapped by the pyenv script, which was used the same way virtualenv was used before it came along. BUT THEN: 

"The pyvenv script has been deprecated as of Python 3.6 in favor of using python3 -m venv to help prevent any potential confusion as to which Python interpreter a virtual environment will be based on." [SOURCE](https://docs.python.org/3/library/venv.html)

So since python 3.6 simply using venv is the recommended way of doing things. Which is what we will be doing. And what I had to slowly find out after going through all the aforemantioned stages. (I think I am now at "acceptance".)

## Boring! Give me the details.

Okay. Pull the repo, switch to this branch, which s still called virtualenv for historical reasons. Type: 

`python3 -m venv env`

NOTE: If python 3 is your standard version which is called when you type `python` you can use that instead of `python3`

then

`source env/bin/activate`

NOTE: On Windows, you probably need backslashes? I don't know.

then

`pip install -r requirements.txt`

NOTE: If you run into trouble, just `pip install` the following packages: tensorflow, keras, matplotlib, scipy, Pillow, h5py

then

`cd code/notebooks`

then

`jupyter notebook`

That should be it. You should now see the Jupyter interfaces in your browser.
