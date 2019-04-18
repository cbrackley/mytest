#!/usr/bin/env python

import setuptools

long_description = "hello"

setuptools.setup(name='mytest',
                 version='1.1.1',
                 description='Analysis of Capture-C data',
                 long_description=long_description,
                 long_description_content_type="text/x-rst",
                 author='Chris Brackley',
                 author_email='C.Brackley@ed.ac.uk',
                 url='https://git.ecdf.ed.ac.uk/cbrackle/capC-MAP',
                 packages=['teststuff'],
                 include_package_data=True,
                 classifiers=[
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                 ],
             )
