import serial
import serial.tools.list_ports

class ConnectArduino:
    """ Automatically find and connect to Arduino to communicate through the PySerial module. """

    def __init__(self):
        """ Initialize serial communication variables. Used to find and connect to serial port """
        self.ports = []
        self.comm_port = None
        self.ser = None

    def get_ports():
        """ Use PySerial module to list detected Serial Comm ports. Return found ports. """
        self.ports = serial.tools.list_ports.comports()
        return self.ports

    def find_arduino(self):
        """ Find 'Arduino' string in the found ports and return port information to connect """
        for port in self.ports:
            port_str = str(port)
            if "Arduino" in port_str: 
                self.comm_port = port_str.split.split(' ')[0]
                return self.comm_port
        return None
    
    def connect_arduino(self):
        """ If the Arduino connection is found, then connect to the Serial Port """        
        if self.comm_port:
            self.ser = serial.Serial(self.comm_port,baudrate = 9600, timeout=1)
            print(f"Connected to {self.comm_port}")
        else:
            print("Connection Issue!")