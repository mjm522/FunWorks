import socket
from struct import *
import numpy as np
import time
import threading
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Format: [ X Acceleration, Y Acceleration, Z Acceleration, X Gravity, Y Gravity, Z Gravity, X Rotation Rate, Y Rotation Rate, Z Rotation Rate, X Orientation (Azimuth), Y Orientation (Pitch), Z Orientation (Roll), deprecated, deprecated, Ambient Light, Proximity, Keyboard Buttons 1 - 8]
"""

#UDP_IP = "96.49.100.238"
#UDP_IP = "127.0.0.1"
UDP_IP = socket.gethostbyname(socket.gethostname())
# print UDP_IP
#print "Receiver IP: ", UDP_IP
#UDP_PORT = 6000
UDP_PORT = 12345#int(raw_input ("Enter Port "))
#print "Port: ", UDP_PORT   
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

accArray = []
graArray = []
rotArray = []
oriArray = np.array([[0],[0],[0]])

def socketListener():
    print "HERE"
    global oriArray
    while True:
        print "HA HA HA H"
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "received message:", data    
        #print "received message: %1.3f %1.3f %1.3f %1.3f", unpack_from ('!f', data, 0), unpack_from ('!f', data, 4), unpack_from ('!f', data, 8), unpack_from ('!f', data, 12)     
        accleration = np.array([unpack_from ('!f', data, 0),unpack_from ('!f', data, 4),unpack_from ('!f', data, 8)])
        gravity = np.array([unpack_from ('!f', data, 12),unpack_from ('!f', data, 16),unpack_from ('!f', data, 20)])
        rotation = np.array([unpack_from ('!f', data, 24),unpack_from ('!f', data, 28),unpack_from ('!f', data, 32)])
        orientation = np.array([unpack_from ('!f', data, 36),unpack_from ('!f', data, 40),unpack_from ('!f', data, 44)])
        oriArray = np.hstack((oriArray,orientation))
        print "Acceleration vectori \n", accleration
        print "Gravity vector \n", gravity
        print "Rotation Rate vector \n", rotation
        print "Orientation \n", orientation


if __name__ == '__main__':
    thread = threading.Thread(target=socketListener)
    thread.daemon = True
    thread.start()
    fig = plt.figure() 
    ax0 = fig.add_subplot(111, projection='3d')
    ax0.set_xlim3d(-120, 120)
    ax0.set_ylim3d(-120, 120)
    ax0.set_zlim3d(-120, 120)
    ax0.set_xlabel('Azimuth')
    ax0.set_ylabel('Pitch')
    ax0.set_zlabel('Roll')
    ax0.set_title('Orientation reading')
    #ax0 = fig.add_subplot(111, projection='3d')
    plt.ion()
    plt.show()
    while True:
        plt.pause(1)
        ax0.scatter(oriArray[0,:],oriArray[1,:],oriArray[2,:],color='r')
        plt.draw()