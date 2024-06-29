from flask import Flask, render_template, request
import subprocess
import os
import signal

app = Flask(__name__)
process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global process
    if process is None or process.poll() is not None:
        process = subprocess.Popen(['python', 'test.py'])
    return 'Started'

@app.route('/stop', methods=['POST'])
def stop():
    global process
    if process is not None and process.poll() is None:
        os.kill(process.pid, signal.SIGTERM)
        process = None
    return 'Stopped'

if __name__ == '__main__':
    app.run(debug=True)
