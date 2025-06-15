# BMP180 to AWS Sensor Dashboard

## Description
This project collects temperature, pressure, and altitude data from a BMP180 sensor connected to a Raspberry Pi. The Pi sends the sensor readings to an AWS EC2 instance running a Flask server. The server stores and serves the data via a REST API using HTTP GET and POST methods, and hosts a web dashboard to visualize the real-time sensor data with interactive charts.

## Hardware
- Raspberry Pi 3 Model B+
- BMP180 Barometric Pressure and Temperature Sensor
- Connection via I2C interface

## Software
- Raspberry Pi:
  - Python scripts to read BMP180 data
  - HTTP client that sends data using POST requests and fetches data using GET requests to AWS Flask server
- AWS EC2:
  - Flask server implementing REST API endpoints with GET and POST methods to receive, store, and serve sensor data
  - Web dashboard built with Chart.js for real-time graphs

## Installation and Setup

### On Raspberry Pi
1. Connect BMP180 sensor via I2C to Raspberry Pi.
2. Install required Python libraries:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install requests smbus2
