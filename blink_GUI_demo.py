# Standard Imports
import tkinter as tk

# Local Imports
from find_arduino_v2 import ConnectArduino

# ---------------------------------------------------------------------------
# Initialize and connect to the Arduino board
# ---------------------------------------------------------------------------

connect_to_arduino = ConnectArduino()
connect_to_arduino.get_ports()     
connect_to_arduino.find_arduino()
connect_to_arduino.connect_arduino()


# ---------------------------------------------------------------------------
# LED control functions
# These functions send single-character commands to the Arduino.
# ---------------------------------------------------------------------------

def turn_on_LED():
    # Send command to turn on-board LED on
    connect_to_arduino.ser.write(b'o')

def turn_off_LED(): 
    # Send command to turn on-board LED off
    connect_to_arduino.ser.write(b'x')

# ---------------------------------------------------------------------------
# GUI Setup
# Create a simple Tkinter window with two buttons to toggle the LED.
# ---------------------------------------------------------------------------

# Create tkinter window, add title, on/off buttons, and set size of GUI.
root = tk.Tk() 
root.title('Blink GUI')

btn_on= tk.Button(root, text="Turn On", command=turn_on_LED)
btn_on.grid(row=0, column=0)

btn_off = tk.Button(root, text="Turn Off", command=turn_off_LED)
btn_off.grid(row=0, column=1)

root.geometry("250x250")
root.mainloop()