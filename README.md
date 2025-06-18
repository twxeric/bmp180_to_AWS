# BMP180 to AWS Sensor Dashboard

## Description
This project collects temperature, pressure, and altitude data from a BMP180 sensor connected to a Raspberry Pi. The Pi sends the sensor readings to an AWS EC2 instance running a Flask server. The server stores and serves the data via a REST API using HTTP GET and POST methods, and hosts a web dashboard to visualize the real-time sensor data with interactive charts.

## Repository Structure

- `bmp180.py` — Python module for reading data from BMP180 sensor on Raspberry Pi.  
- `server_client.py` — Python script running on Raspberry Pi, reads sensor and sends data to AWS.  
- `main.py` — Flask application running on AWS, serves REST API and web dashboard.  
- `templates/` — Contains HTML dashboard page.  
- `static/` — (optional) Static files such as CSS or JS if needed.  

---


## Hardware
- Raspberry Pi 3 Model B+  
- BMP180 Barometric Pressure and Temperature Sensor  
- Connection via I2C interface
  

## Software
- **Raspberry Pi**  
  - Python scripts to read BMP180 data  
  - HTTP client that sends data using POST requests and fetches data using GET requests to AWS Flask server  
- **AWS EC2**  
  - Flask server implementing REST API endpoints with GET and POST methods to receive, store, and serve sensor data  
  - Web dashboard built with Chart.js for real-time graphs  

---

## Prerequisites

### On Raspberry Pi
- Raspberry Pi running Raspbian OS.  
- BMP180 sensor connected via I2C.  
- Python 3 installed.  

### On AWS Server
- Python 3 environment.  
- Flask installed.  
- Publicly accessible EC2 instance with HTTP port open.  

---

## Setup Instructions

### 1. Configure Raspberry Pi
- Connect BMP180 sensor to Raspberry Pi I2C pins.  
- Enable I2C interface:  
  ```bash
  sudo raspi-config
  # Navigate to Interface Options -> I2C -> Enable
  
### 2. Create and activate a virtual environment in VM AWS
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
### 3. Install required Python libraries
  ```bahs
  sudo apt-get update
  sudo apt-get install python3-pip i2c-tools
  pip3 install smbus2 requests flask
  pip install flask-cors

  ```
### 4. Test BMP180 sensor reading in RpPi
Run the provided bmp180.py script to verify you can read sensor values:
  ```bahs
  python3 bmp180.py
  ```
### 5. Start Flask server on AWS
  ```bahs
  flask --app main run --host 0.0.0.0
  ```

### 6. Configure and run Raspberry Pi client
Edit [`server_client.py`](./server_client.py), updating API_URL to point at your AWS server (e.g. http://<EC2_PUBLIC_IP>:5000/data).
Run the client script:
  ```bahs
  python3 server_client.py
  ```

## Usage
Open your browser and navigate to:
  ```bahs
  http://<EC2_PUBLIC_IP>:5000/
  ```
You’ll see three real‑time charts for temperature, pressure, and altitude updating every 2 seconds.
Hover over points to see exact values in tooltips.


## Troubleshooting
- I2C errors: run i2cdetect -y 1 to confirm sensor visibility.
- Network issues: ensure Pi can reach EC2 and EC2 security group allows connections.
- Flask errors: check server logs in the terminal where you ran main.py.
- JavaScript errors: open browser console and verify Chart.js loads without errors.
  
