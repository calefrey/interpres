import serial

def read(serial_port):  #should return a 1d array of sensor values
    ser = serial.Serial(serial_port, 115200)
    #ser.open()
    line = ser.readline()
    #ser.close()

    """
    Returns an array of the current sensor data from tue arduino
    """
    return line.split(",") #[1,2,3,4,5,6,7,8,9,0] # used for testing
