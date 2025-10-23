from setuptools import setup,find_packages
from typing import list 

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [ file.replace("/n","") for file in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='ml project 2',
    version='0.0.1',
    author='raibhaskar',
    author_email='iamraibhaskar@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)
