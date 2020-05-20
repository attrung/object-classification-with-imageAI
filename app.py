import os
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

# path to static folder (for image static)
UPLOAD_FOLDER = r'C:\Users\John Nguyen\Documents\GitHub\object-classification-with-imageAI\static\upload'

# allowed image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg'} # allows png and jpg files

# app configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/uploadImage', methods = ['POST'])
def postImage():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # if there is a file, we save it for later analysis
        ext = file.filename.split('.')[-1]
        if file and ext in ALLOWED_EXTENSIONS:
            global filename
            filename = "image" + '.' + ext
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename = filename))

@app.route('/analyzeImage')
def uploaded_file():
    return render_template("main.html", filename = filename)

if __name__ == '__main__':
    app.run("localhost", 5000, debug = False)