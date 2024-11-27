from flask import Flask
from config import config
import serial
import time
import threading


app = Flask(__name__)
lock = threading.Lock()
is_running = false

def send_serial_data(str1, str2):
    with serial.Serial(config.tty, 19200, timeout=1) as ser:
        print(ser.name)         # check which port was really used
        ser.write(f'\r{str1} \r'.encode())  # write str1
        ser.write(str2.encode())            # write str2
        ser.close()             # close port

def send_greeting(str1, str2):
    with serial.Serial(config.tty, 19200, timeout=1) as ser:
        print(ser.name)         # check which port was really used
        ser.write(f'\r{str1} \r'.encode())  # write str1
        ser.write(str2.encode())            # write str2
        ser.close()             # close port

@app.route('/entering/<str2>', methods=['GET'])
def entering(str2):
    str1 = "Now Entering:"  # You can set str1 to any fixed value or pass it as needed
    send_greeting(str1, str2)
    return f"Sent str2: {str2} to the serial port", 200

@app.route('/display/<str1>:<str2>', methods=['GET'])
def display(str1, str2):
    send_serial_data(str1, str2)
    return f"Sent str1: {str1} and str2: {str2} to the serial port", 200

if __name__ == '__main__':
    app.run(debug=True)