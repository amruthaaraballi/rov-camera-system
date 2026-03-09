from setuptools import setup
import os
from glob import glob

package_name = 'rov'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amrutha',
    description='ROV camera streaming system',
    license='Apache 2.0',

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],

    entry_points={
        'console_scripts': [
            'camera = rov.camera:main',
            'mavros = rov.mavros:main',
            'website = rov.website:main',
        ],
    },
)