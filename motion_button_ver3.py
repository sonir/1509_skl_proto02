#import libraries
import smbus
import time
import OSC
import RPi.GPIO as GPIO

#Define Sysrtem Variables
port = 5678
#ip_adr = '127.0.0.1'
ip_adr = '224.0.0.1'

#Setup GPIOS
GPIO.setmode(GPIO.BOARD)
SW = 7
GPIO.setup(SW, GPIO.IN)


#create instance of smbus
bus = smbus.SMBus(1)

#IC address
address = 0x1D

#addresses of each axis
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

#inicialize senser
def init_ADXL345():
    bus.write_byte_data(address, 0x2D, 0x08)


#get data from IC
def measure_acc(adr):
    #read lower bytes of each axis
    acc0 = bus.read_byte_data(address, adr)
    #read higer bytes of each axis
    acc1 = bus.read_byte_data(address, adr + 1)

    #unite 2byte datas into 10byte
    acc = (acc1 << 8) + acc0

    #check if 10th byte is 10
    if acc > 0x1FF:
        #minus
        acc = (65536 - acc) * -1

    acc = acc * 3.9/1000

    return acc



client = OSC.OSCClient()
OSCaddress = (ip_adr, port)
#OSCaddress2 = ('192.168.0.2', 5678)

init_ADXL345()

try:
    while(1):
        key_in = GPIO.input(SW)
        msg = OSC.OSCMessage()
        if key_in == 1:
            msg.setAddress("/sw")
            msg.append(key_in)

            client.sendto(msg, OSCaddress)
            time.sleep(2)

            msg = OSC.OSCMessage()
            msg.setAddress("/sw")
            msg.append(0)

            client.sendto(msg, OSCaddress)

        else:
            x_acc = measure_acc(x_adr)
            y_acc = measure_acc(y_adr)
            z_acc = measure_acc(z_adr)

            msg.setAddress("/acs/motion")

            # msg.append(x_acc)
            # msg.append(y_acc)
            # msg.append(z_acc)
            3d_acc = (x_acc*y_acc*z_acc)
            msg.append(3d_acc)
            client.sendto(msg, OSCaddress)
            print(3d_acc+"\n")

            time.sleep(0.01)

    #print 'X = %2.2f' % x_acc, '[g], Y = %2.2f]' % y_acc,'[g], Z = %2.2f' % z_acc, '[g]'



except KeyboardInterrupt:
    pass
