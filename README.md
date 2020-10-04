# miURL

miURL is a web application project developed with Python that allows users to create a custom, 
short URL and copy it to the clipboard of their device for pasting. Users can create
a URL that links to another website or a file. The application was designed and built with 
Python’s Flask web framework, JSON, and clipboard.js. 


## Table of Contents

* [Installation](https://github.com/t-mcneal/miurl/blob/master/README.md#installation)
* [Usage](https://github.com/t-mcneal/miurl/blob/master/README.md#usage)
* [Demo](https://github.com/t-mcneal/miurl/blob/master/README.md#demo)


## Installation

1. **Install Python 3**

    If not currently installed on your computer, download and install Python 3 at [Python.org](https://www.python.org/downloads/).

2. **Download Project**

    To install the miURL project locally, download a zip of the project from github or clone the repository.

3. **Create a Virtual Environment**

    It is best to locally run a Flask application using a virtual environement. To get setup with a virtual 
    environment, follow the quick [guide](https://flask.palletsprojects.com/en/1.1.x/installation/#installation) 
    on the Flask website, which has instructions for both Windows and Mac OS X. The guide will walk you through 
    how to create a virtual environement within the project directory and install Flask in the environment. 
    
    >> **Note:** the Flask guide uses the command line. If you are not familiar with terminal commands, read this 
    >> [blog](https://scotch.io/bar-talk/10-need-to-know-mac-terminal-commands) by scotch.io to learn 10 commonly
    >> used terminal commands - #10 is a fun one!

4. **Edit *app.py* File**

    Last, you will need to make a quick edit to the *app.py* file located in the project. In addition to creating
    short URLs that link to a web page, miURL also allows users to upload and create URLs for PDF, PNG, JPEG, JPG, 
    or GIF files! In order for this feature to occur, a storage location is needed.

    Within the project, there is a *user_files* directory located in the *static* directory. The *user_files* 
    acts as a the storage location for users' uploaded files. In deployment, this storage setup would be handled 
    differently. For the purpose of running this project locally, the *user_files* directory will store 
    any files uploaded to the miURL application.

    ### Instrucions for Edit

    To make the edit, open the *app.py* Python file. Near the top of the file, you should see the below code.
    For `app.config['USER_FILES']`, replace the string `'path/miurl/static/user_files/'` by inserting a string
    of your computer's absolute file path to the *user_files* directory, located in the project's *static* directory.

    ```python 
    # NOTE: Insert your computer's absolute file path to the "user_files" directory located 
    # in the "static" directory
    app.config['USER_FILES'] = 'path/miurl/static/user_files/'
    ```

    If you are unfamiliar with how to get absolute file paths for directories, use one of the following links below.

    * [Mac OS X](https://macpaw.com/how-to/get-file-path-mac)
    * [Windows](https://www.sony.com/electronics/support/articles/00015251)

    Once making the above edit, be sure to save the *app.py* file.


## Usage

Next, you will need to run the miURL Flask application in your newly created virtual environment.
Use the command line to access the project folder and start the virtual environment. Once you have
started the virtual environment, you can now run the app to startup the local server using the 
following command line syntax.

```
$ export FLASK_ENV=development
$ flask run
```

This step enables the development environment, including the interactive debugger and reloader, and then starts the server on `http://localhost:5000/`. Copy the server link from the command line, then place it in your browser to access the miURL web app. To view how to interact with the app and it's features, watch the demo below.


## Demo

Watch the video below to see a demo!

[![Watch the video](https://drive.google.com/file/d/1JvqEKncR87-BHkGu8he5cyyyD3voJSB_/view?usp=sharing)](https://youtu.be/arbSqG113i0)


## License

[MIT](https://choosealicense.com/licenses/mit/)























