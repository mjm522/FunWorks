import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import socket, traceback

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

timeArray = []
accArray = []
gyroArray = []
magArray = []
itr = 0
while itr < 400:
    itr += 1
    try:
        message, address = s.recvfrom(8192)
        parseMsg = message.split(",")
        timeStamp = float(parseMsg[0])
        accelerometer = parseMsg[2:5]
        accelerometer = np.asarray([float(i) for i in accelerometer])
        gyro = parseMsg[6:9]
        gyro = np.asarray([float(i) for i in gyro])
        magneto = parseMsg[10:13]
        magneto = np.asarray([float(i) for i in magneto])
        timeArray.append(timeStamp)
        accArray.append(accelerometer)
        gyroArray.append(gyro)
        magArray.append(magneto)
        print itr
        '''print "timeStamp\t", timeStamp
        print "accelerometer\t", accelerometer
        print "gyro\t", gyro
        print "magneto\t",magneto'''
    except (KeyboardInterrupt, SystemExit):
        raise "something went wrong"
accArray = np.asarray(accArray)
gyroArray = np.asarray(gyroArray)
magArray = np.asarray(magArray)

fig = plt.figure()
ax0 = fig.add_subplot(121, projection='3d')
ax0.plot(accArray[:,0],accArray[:,1],accArray[:,2])
ax0.set_xlim3d(0, 10)
ax0.set_ylim3d(0, 10)
ax0.set_zlim3d(0, 10)

ax0.set_xlabel('X axis')
ax0.set_ylabel('Y axis')
ax0.set_zlabel('Z axis')
ax0.set_title('Accelerometer reading')

ax1 = fig.add_subplot(122, projection='3d')
ax1.plot(gyroArray[:,0],gyroArray[:,1],gyroArray[:,2])
ax1.set_xlim3d(-1, 1)
ax1.set_ylim3d(-1, 1)
ax1.set_zlim3d(-1, 1)

ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')
ax1.set_title('Gyro reading')
plt.show()