#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['imu_send_tf']
d['package_dir'] = {'': 'src'}

setup(**d)
