import os, shutil
from flask import Flask, render_template, request, redirect, flash, url_for
from objectDetection import objectDetection
from createGraph import createGraph
import random

# counter to set file name (avoiding cache)
counter = int(random.random()*10000000)

app = Flask(__name__)

# path to static folder (for image static)
image_folder = 'static/image/'

# allowed image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg'} # allows png and jpg files

# app configuration
app.config['image_folder'] = image_folder
app.config['file_counter'] = counter
app.secret_key = "development key"

@app.route('/')
def main():
    app.config['file_counter'] += 1
    for filename in os.listdir(image_folder):
        file_path = os.path.join(image_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return render_template("index.html")

@app.route('/uploadImage', methods = ['POST'])
def postImage():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
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
            filename = str(app.config['file_counter']) + "." + ext
            file.save(os.path.join(app.config['image_folder'], filename))
            return redirect(url_for('analyzeImage'))

@app.route('/analyzeImage')
def analyzeImage():
    output_filename = filename.split('.')[0] + "_output" + '.png'
    prob = 50
    final_label, final_prob = objectDetection(filename, output_filename, prob)
    graph_filename = filename.split('.')[0] + "_graph" + '.png'
    ans = createGraph(final_label, final_prob, graph_filename)
    return render_template("main.html", output = output_filename, graph = graph_filename)

@app.route('/displayImage/<filename>')
def displayImage(filename):
    return redirect(url_for('static', filename='image/' + filename))

if __name__ == '__main__':
    app.run("localhost", 5000, debug = True)