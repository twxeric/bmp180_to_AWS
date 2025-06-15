# BMP180 Sensor Data to AWS

This project collects environmental data from a BMP180 sensor (temperature, pressure, and altitude) using a Raspberry Pi and sends it to a Flask server running on an AWS virtual machine (VM). The server stores and exposes the latest reading using GET and POST HTTP methods.

## Project Structure
bmp180-to-aws/
├── bmp180.py             # Reads BMP180 sensor data via I2C
├── server_client.py      # Runs on Raspberry Pi, sends data to AWS via POST
├── main.py               # Flask server on AWS VM, handles GET and POST
├── requirements.txt      # Python dependencies for both Pi and VM
├── .gitignore            # Files to ignore in GitHub
└── README.md             # This file
