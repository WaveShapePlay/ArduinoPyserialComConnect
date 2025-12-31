# Standard Import
import time

# Third Party Import
import serial
import serial.tools.list_ports


class ConnectArduino:
    """ Automatically find and connect to Arduino to communicate through the PySerial module. 
    
    This class handles:
    - Listing available serial ports
    - Searching for board related keywords - keyword must match connection description
    - Connecting to the matching port
    """

    def __init__(self):
        """ Initialize serial communication variables. Used to find and connect to serial port """

        # Board description keyword list to search for in detection connections
        self.board_keywords = ["Arduino", "UNO", "R4"]

        # List for found serial ports found
        self.ports = []

        # Detected port (Example - Windows OS: "COM3" or MacOS "/dev/cu.usbmodemXYZ")
        self.comm_port = None

        # Serial connection object
        self.ser = None

    def get_ports(self):
        """ 
        Use PySerial module to list detected Serial Comm ports. Return found ports.

        Returns:
            list: A list of objects representing detected ports. 

        """
        self.ports = serial.tools.list_ports.comports()
        return self.ports

    def find_arduino(self):
        """ Find board keyword string in the found ports and return port information to connect
            
            Returns:
                str or None: If serial port description contains keyword then connect, else return None 
        """
        for port in self.ports:
            port_str = str(port)
            if any(keyword in port_str for keyword in self.board_keywords):
                self.comm_port = port_str.split(' ')[0] # Get port name of detected board based on keyword list
                return self.comm_port
        return None

    def connect_arduino(self):
        """ If the Arduino connection is found, then connect to the Serial Port """        
        if self.comm_port:
            self.ser = serial.Serial(self.comm_port, baudrate=9600, timeout=1) # Serial connection parameters 
            print(f"Connected to {self.comm_port}")
        else:
            print("Connection Issue!")



# ---------------------------------------------------------------------------
# Debug / Test Code
# This block only runs when Python script is ran directly as a stand alone file.
# It will not run when imported by another script.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    This test code is the essentials of what is needed to connect using the find_arduino_v2 file.
    The Try/Except statement will blink and keep the Arduino on-board LED on for visual confirmation.
    time.sleep() controls duration of the LED being on/off and first delay gives time for the board 
    to initialize the serial connection.
    """
    connect_to_arduino = ConnectArduino()

    # Step 1: Look for ports connected to Computer
    connect_to_arduino.get_ports()

    # Step 2: Search for Arduino board keywords in list (self.board_keywords)
    connect_to_arduino.find_arduino()

    # Step 3: Use desteted port to connect or print "Connection Issue!
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
