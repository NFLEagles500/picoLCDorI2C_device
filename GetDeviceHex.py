'''Get hex address of device.  I had issues with an lcd device before because the script that came with the device assumed 0x27 for the device hex address, which was incorrect.
Use this script to get the correct address

When you init the device, the script below will return the addr= value
'''
import machine
sdaPIN=machine.Pin(0)
sclPIN=machine.Pin(1)
i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
devices = i2c.scan()
if len(devices) == 0:
 print("No i2c device !")
else:
 print('i2c devices found:',len(devices))
for device in devices:
 print("Hexa address: ",hex(device))
