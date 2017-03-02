import socket
from struct import *
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Format: [ X Acceleration, Y Acceleration, Z Acceleration, 
X Gravity, Y Gravity, Z Gravity, 
X Rotation Rate, Y Rotation Rate, Z Rotation Rate, 
X Orientation (Azimuth), Y Orientation (Pitch), Z Orientation (Roll), 
deprecated, deprecated, Ambient Light, Proximity, Keyboard Buttons 1 - 8]
"""

#UDP_IP = "96.49.100.238"
#UDP_IP = "127.0.0.1"
UDP_IP = socket.gethostbyname(socket.gethostname())
#print "Receiver IP: ", UDP_IP
#UDP_PORT = 6000
UDP_PORT = 5555#int(raw_input ("Enter Port "))
#print "Port: ", UDP_PORT   
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

accArray = np.array([[0],[0],[0]])
graArray = np.array([[0],[0],[0]])
rotArray = np.array([[0],[0],[0]])
oriArray = np.array([[0],[0],[0]])
posArray = np.zeros((3,351))

itr = 0
while itr<350:
    itr += 1
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data    
    #print "received message: %1.3f %1.3f %1.3f %1.3f", unpack_from ('!f', data, 0), unpack_from ('!f', data, 4), unpack_from ('!f', data, 8), unpack_from ('!f', data, 12)     
    accleration = np.array([unpack_from ('!f', data, 0),unpack_from ('!f', data, 4),unpack_from ('!f', data, 8)])
    gravity = np.array([unpack_from ('!f', data, 12),unpack_from ('!f', data, 16),unpack_from ('!f', data, 20)])
    rotation = np.array([unpack_from ('!f', data, 24),unpack_from ('!f', data, 28),unpack_from ('!f', data, 32)])
    orientation = np.array([unpack_from ('!f', data, 36),unpack_from ('!f', data, 40),unpack_from ('!f', data, 44)])
    oriArray = np.hstack((oriArray,orientation))
    accArray = np.hstack((accArray,orientation))
    graArray = np.hstack((graArray,orientation))
    rotArray = np.hstack((rotArray,orientation))
    print itr
    '''print "Acceleration vectori \n", accleration
    print "Gravity vector \n", gravity
    print "Rotation Rate vector \n", rotation
    print "Orientation \n", orientation'''


for i in range(accArray.shape[1]-1):
    posArray[:,i+1] = posArray[:,i] + accArray[:,i] 


fig = plt.figure() 
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_title('Surface moved')

X, Y = np.meshgrid(posArray[0,:], posArray[1,:])
surf = ax0.plot_surface(X, Y, posArray[2,:],             # data values (2D Arryas)
                       rstride=2,           # row step size
                       cstride=2,           # column step size
                       cmap=cm.RdPu,        # colour map
                       linewidth=1,         # wireframe line width
                       antialiased=True)
plt.show()
