from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colorize', methods=['POST'])
def colorize():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    img_path = os.path.join('static', 'temp_image.jpg')
    file.save(img_path)

    output_path = os.path.join('static', 'colorized_image.jpg')
    subprocess.run(['python', 'colorize.py', '-i', img_path, '-o', output_path, '-r', '360'])

    return redirect(url_for('show_colorized'))

@app.route('/show_colorized')
def show_colorized():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
