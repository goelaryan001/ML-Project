#So with the help of setup.py, I will be able to build my entire machine learning application as a package

from setuptools import find_packages, setup
#So this will automatically find out all the packages that are available in the, in the entire, uh, in the entire machine learning application in the directory that we have actually created.
from typing import List

hyphen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
#this last line is done to remove \n which comes with going to next line in requirements.ext file like while jumping from pandas to numpy which is reading the next line \n also tags along while reading.
        if hyphen_e_dot in requirements:
           requirements.remove(hyphen_e_dot)
    return requirements

setup(
name='ML Project',
version='0.0.1',
author='Aryan',
author_email='goel.aryan001@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
#install_requires=['pandas','numpy','seaborn'] now if we require 100 or more packages it is hard to 
#add so many manually so we use a function