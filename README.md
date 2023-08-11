# APIs
These are any APIs I might create. More often than not, it's gonna be used on lunauwu.net.
Please note: These python scripts are ***DEVELOPMENT SERVERS***, as such they can be reworked by you to fit your needs. The development server is designed for testing and debugging purposes and is not as performant and secure as a production-ready WSGI server like Gunicorn or uWSGI.

# Step by step guide to set up API servers up using Gunicorn:

1. Install Gunicorn:\
Open a terminal and run the following command to install Gunicorn:\
```sudo apt install gunicorn```

2. Create a service file for your API:\
```sudo nano /etc/systemd/system/api.service```

3. In the nano editor, paste the following content for the service unit:
```[Unit]
Description=API Service
After=network.target

[Service]
User=luna
WorkingDirectory=/home/luna
ExecStart=/usr/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 api:app
Restart=always

[Install]
WantedBy=multi-user.target
```
Replace `luna` with your actual username in the `User=` field.\
Replace `/home/luna` with your actual working direcory in the `WorkingDirectory=` field.\
Replace `0.0.0.0:5000` with your actual bind port in the `ExecStart=` field.\
Replace `api:app` with your actual API name in the `ExecStart=` field, using the format `apiPythonFileName:app`. You should not include `.py` here.

4. Reload Systemd and enable the Service:\
```sudo systemctl daemon-reload```\
```sudo systemctl enable api.service```

5. Start the service, then check the service status:\
`sudo systemctl start api.service`\
`sudo systemctl status api.service`

If everything was done correctly, you should now have a working API server.\
This API server would also start when your machine boots, right after network, assuming you'll be using the service template provided here.