import serial.tools.list_ports
from SC import usbCommunication

def findSerialNumber():
    for pInfo in serial.tools.list_ports.comports():
        if "Arduino" in pInfo.description:
            return pInfo.serial_number;
    print("No Arduino detected")
    return "0"

def findArduinoPort(serial_number):
    for portInfo in serial.tools.list_ports.comports():
        if portInfo.serial_number == serial_number:
            return serial.Serial(portInfo.device).port
    raise IOError("Could not find an arduino - is it plugged in?")


ArduinoSerialNumber = findSerialNumber();
ArduinoPort = findArduinoPort(ArduinoSerialNumber);


test = usbCommunication(ArduinoPort, 115200);

while(True):#
     msg = input("Input Command: ")
     test.sendMessage(msg)
