import serial
import serial.tools.list_ports
import time

class ConnectArduino:
    """ Automatically find and connect to Arduino to communicate through the PySerial module. """

    def __init__(self):
        """ Initialize serial communication variables. Used to find and connect to serial port """
        self.board_keywords = ["Arduino", "UNO", "R4"]
        self.ports = []
        self.comm_port = None
        self.ser = None

    def get_ports(self):
        """ Use PySerial module to list detected Serial Comm ports. Return found ports. """
        self.ports = serial.tools.list_ports.comports()
        return self.ports

    def find_arduino(self):
        """ Find board keyword string in the found ports and return port information to connect """
        for port in self.ports:
            port_str = str(port)
            if any(keyword in port_str for keyword in self.board_keywords):
                self.comm_port = port_str.split(' ')[0]
                return self.comm_port
        return None

    def connect_arduino(self):
        """ If the Arduino connection is found, then connect to the Serial Port """        
        if self.comm_port:
            self.ser = serial.Serial(self.comm_port,baudrate = 9600, timeout=1)
            print(f"Connected to {self.comm_port}")
        else:
            print("Connection Issue!")


'''
#Debug Test Code:

connect_to_arduino = ConnectArduino()
connect_to_arduino.get_ports()
connect_to_arduino.find_arduino()
connect_to_arduino.connect_arduino()

try:
    time.sleep(1)
    connect_to_arduino.ser.write(b'o')
    time.sleep(2)
    connect_to_arduino.ser.write(b'x')
    time.sleep(1)
    connect_to_arduino.ser.write(b'o')
except:
    print("Error in connection or detection")
'''
