import os
import psutil
import time
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='/var/www/sysmonitor')
CORS(app)  # Enable CORS for all routes

def get_system_details():
    cpu_percent = psutil.cpu_percent(interval=None, percpu=False)
    memory = psutil.virtual_memory()
    drives = {}
    for drive in psutil.disk_partitions(all=False):
        if not drive.device.startswith('/dev/loop'):
            drive_info = psutil.disk_usage(drive.mountpoint)
            drives[drive.device] = {
                'total': round(drive_info.total / (1024 ** 3), 2),
                'used': round(drive_info.used / (1024 ** 3), 2),
                'free': round(drive_info.free / (1024 ** 3), 2),
                'percent': drive_info.percent
            }

    return {
        'cpu_percent': cpu_percent,
        'memory': {
            'percent': memory.percent
        },
        'drives': drives
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system_details')
def system_details():
    details = get_system_details()
    return jsonify(details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)