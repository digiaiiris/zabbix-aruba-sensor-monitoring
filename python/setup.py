#!/usr/bin/python

# Python imports
import os
from setuptools import setup

setup(
    name="aruba-sensor-monitoring",
    version="1.0.1",
    author="Antti-Pekka Meronen",
    author_email="antti-pekka.meronen@digia.com",
    description="Monitoring scripts for Aruba sensors",
    url="https://github.com/digiaiiris/zabbix-aruba-sensor-monitoring/",
    license="MIT",
    packages=["ic_aruba"],
    entry_points={
        "console_scripts": [
            "aruba_discover_sensors = ic_aruba.aruba_discover_sensors:main",
            "aruba_sensor = ic_aruba.aruba_sensor:main"
        ]
    },
    install_requires=[
        'requests>=2.22.0'
    ]
)
