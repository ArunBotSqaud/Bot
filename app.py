from flask import Flask, render_template, request
import nbformat
from nbconvert import HTMLExporter
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_notebook', methods=['POST'])
def run_notebook():
    # Path to your notebook
    notebook_path = 'gemma_connection_ChatBot.ipynb'

    # Execute the notebook using nbconvert
    try:
        subprocess.run(['jupyter', 'nbconvert', '--to', 'html', '--execute', notebook_path])
        with open(notebook_path.replace('.ipynb', '.html'), 'r') as f:
            notebook_html = f.read()
        return notebook_html
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
