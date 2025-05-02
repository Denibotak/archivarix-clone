from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    # File yang akan diunduh, misalnya file.zip
    file_path = 'archivarix.zip'
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
