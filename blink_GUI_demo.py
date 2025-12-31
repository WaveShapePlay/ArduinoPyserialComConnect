# Standard Imports
import tkinter as tk

# Local Imports
from find_arduino_v2 import ConnectArduino

# Connect to the Arduino board
connect_to_arduino = ConnectArduino()
connect_to_arduino.get_ports()
connect_to_arduino.find_arduino()
connect_to_arduino.connect_arduino()

def turnOnLED():
    # Send command to turn on-board LED on
    connect_to_arduino.ser.write(b'o')

def turnOffLED(): 
    # Send command to turn on-board LED off
    connect_to_arduino.ser.write(b'x')

# Create tkinter window, add title, on/off buttons, and set size of GUI.
root = Tk() 
root.title('Blink GUI')

btn_On= tk.Button(root, text="Turn On", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOffLED)
btn_Off.grid(row=0, column=1)

root.geometry("250x250")
root.mainloop()