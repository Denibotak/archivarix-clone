from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    file_path = 'archivarix.zip'
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    # Untuk deployment di Render: gunakan 0.0.0.0 dan PORT dari environment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)