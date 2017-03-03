import tf
import rospy
import socket
import numpy as np
from functools import partial
from struct import unpack_from

'''
Instructions:
Install sensorUDP from playstore 
url: https://play.google.com/store/apps/details?id=com.ubccapstone.sensorUDP&hl=en_GB
the pc and phone should be on same wifi router.
for ease, create a hotspot in the phone
'''

class SendIMUFrameRos():

    def __init__(self, udp_ip='192.168.43.34', udp_port=6000, read_rate=500):

        self._udp_ip = udp_ip
        self._udp_port = udp_port
        self._read_rate = read_rate

        self._socket = None
        self._socket_configured = False
        self._new_data_received = False

        self._linear_acc = None
        self._rotation = None
        self._gravity = None
        self._ori = None
        self._pos = np.array([0.,0.,0.])[:,None]
        self._vel = np.array([0.,0.,0.])[:,None]

        self.configure()

    def configure(self):
        self._old_time  = rospy.get_rostime()
        self._br_tf = tf.TransformBroadcaster()
        self._socket = socket.socket(socket.AF_INET, # Internet
                                     socket.SOCK_DGRAM) # UDP
        self._socket.bind((self._udp_ip, self._udp_port))
        self._socket_configured = True
        update_period = rospy.Duration(1.0/self._read_rate)
        rospy.Timer(update_period, partial(self.socket_listener))
        rospy.Timer(update_period, partial(self.send_coordinate_frame))


    def socket_listener(self, event):
        data = None
        try:
            data, addr  = self._socket.recvfrom(1024)
        except Exception as e:
            pass

        if data is not None:
            self.parse_data(data)


    def parse_data(self, data):
        self._linear_acc  = np.array([unpack_from ('!f', data, 0),unpack_from ('!f', data, 4),unpack_from ('!f', data, 8)])
        self._gravity     = np.array([unpack_from ('!f', data, 12),unpack_from ('!f', data, 16),unpack_from ('!f', data, 20)])
        self._rotation    = np.array([unpack_from ('!f', data, 24),unpack_from ('!f', data, 28),unpack_from ('!f', data, 32)])
        self._ori         = np.array([unpack_from ('!f', data, 36),unpack_from ('!f', data, 40),unpack_from ('!f', data, 44)])
        self._new_data_received = True


    def send_coordinate_frame(self, event):
        if not self._new_data_received:
            return
        self._new_data_received = False
        dt = self.dt()
        self._pos += self._vel*dt + 0.5*self._linear_acc*(dt**2)
        q = tf.transformations.quaternion_from_euler(self._ori[0], self._ori[1], self._ori[2])
        self._br_tf.sendTransform(self._pos.flatten(), q, rospy.Time.now(), 'myphone', 'base')

    def dt(self):
        now = rospy.get_rostime()
        dt =  (now.secs - self._old_time.secs) + (now.nsecs - self._old_time.nsecs)*10e-9
        self._old_time = now
        return dt


def main():
    phone_imu = SendIMUFrameRos()

    while not rospy.is_shutdown():
        pass


if __name__ == '__main__':
    rospy.init_node('send_coordinates')
    main()
