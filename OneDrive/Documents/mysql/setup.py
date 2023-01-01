from setuptools import find_packages,setup

from typing import List

def requirments():
      with open('requirments.txt') as file:
            list1=file.readlines()
            # print(list1)
            list1=[i.replace('\n','') for i in list1]
            # print(list1)
      if '-e .' in list1:
            list1.remove('-e .')
            # print(list1)
            return list1



requirments()

setup(name='class',
      version='0.0.1',
      author='sanju',
      author_email='annapureddysanjeev@gmail.com',
      packages=find_packages(),
      install_requires=requirments(),
      )