from flask import Flask, render_template, request, send_file
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Halaman utama
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        # Panggil API Wayback Machine dan proses data
        return download_from_wayback(url)
    return render_template('index.html')

# Proses download dari Wayback Machine
def download_from_wayback(url):
    # Misalnya kita ingin mengambil snapshot dari Wayback Machine
    wayback_url = f'http://archive.org/web/{url}'
    
    # Proses download atau scrape halaman tersebut
    response = requests.get(wayback_url)
    if response.status_code == 200:
        # Simulasi proses penyimpanan atau manipulasi data di sini
        file_path = 'archivarix.zip'  # Ganti dengan proses yang sesuai untuk membuat ZIP dari Wayback

        # Simpan atau proses file ZIP hasil scrape (misalnya)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        return send_file(file_path, as_attachment=True)
    else:
        return "Error: Tidak dapat mengakses Wayback Machine", 500

if __name__ == "__main__":
    app.run(debug=True)
