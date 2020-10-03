from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)

# NOTE: Change the secret key below to a new random string for security purposes since 
# the "app.py" file is publicly available on GitHub
app.secret_key = b'\xc84\xba\x93\xef\xcdE$v\x0b\x16\xd0\xa4\x94\xd6H\x86!\xc1<\xb4\x85\xba\xe3'

# NOTE: Insert your computer's absolute file path to the "user_files" directory located 
# in the "static" directory
app.config['USER_FILES'] = 'path/miurl/static/user_files/'

app.config['ALLOWED_EXTENSIONS'] = ['pdf', 'png', 'jpg', 'jpeg', 'gif']


# Route to miURL homepage that has the forms to create a short URL
@app.route('/')
def home():
    return render_template('home.html', codes=session.keys())


# Route to a web page displaying the created URL that can also be copied to the clipboard
@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        # Create an empty dictionary to work with JSON.
        urls = {}
        
        # Opens the JSON file 'urls.json' containing created URLs if the file exists.
        # Then, the empty dictianary stores the loaded JSON file.
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        
        # Flash a "short name already taken" message if user tries to enter a short name code 
        # that already exists in the JSON file.
        if request.form['code'] in urls.keys():
            flash('That short name has already been taken. Please select another name.')
            return redirect(url_for('home'))

        # Checks whether the user is creating a short URL for a website or file by checking 
        # the name attribute keys() of a submitted form's <input> tags.
        #
        # 1.) If for a website, write a dictionary to the JSON file with the created
        #     short name code as the KEY, and a second dictionary as the VALUE. The second dictionary 
        #     stores the string 'url' as the KEY and the website url as the VALUE. 
        #
        # 2.) Else the URL is for a file. 
        #     - Create a new filename for the file by concatenating the short name code entered by the 
        #       user and a secured version of the original filename.
        #     - Check if file is an allowed file type of PDF, PNG, JPEG, JPG, or GIF. 
        #     - If file is allowed, the file is then saved into the "user_files" directory. 
        #     - Then, a dictinary is written to the JSON file with the created short name code as the KEY, 
        #       and a second dictionary as the VALUE. The second dictionary stores the string 'file' as the 
        #       KEY and the new concatenated filename as the VALUE.
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            if allowed_file(full_name):
                f.save(os.path.join(app.config['USER_FILES'], full_name))
                urls[request.form['code']] = {'file': full_name}
            else:
                flash('File type must be a PDF, PNG, JPEG, JPG, or GIF.')
                return redirect(url_for('home'))

        # If the JSON file does not exist, the code below creates the file
        # and adds a dictionary containing data from the submitted form.
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
            session[request.form['code']] = True

        # Renders the "your_url.html" web page, and also sends the short name code created 
        # by the user as a variable
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))


# Route to the website or file of a created URL by acessing the data in "urls.json"
@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    return abort(404)


# Route to error 404 "Not Found" web page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# Handles cache of static files
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    """Adds last modified timestamp to static (CSS and JavaScript) links.
    
    Keyword arguments:
    endpoint - directory of files to add time stamps
    **values - keyworded, variable-length argument list of files in the endpoint directory
    """
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


def allowed_file(filename):
    """Returns True if a file type is a PDF, PNG, JPG, JPEG, or GIF. 
    Returns False otherwise.
    
    Keyword arguments:
    filename - name of file
    """
    if filename[-4] == "." or filename[-5] == ".":
        if filename[-4] == ".":
            ext = filename[-3:].lower()  
        else:
            ext = filename[-4:].lower()
        if ext in app.config['ALLOWED_EXTENSIONS']:
                return True
    return False

